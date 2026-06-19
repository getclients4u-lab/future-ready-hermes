"""
Orchestrator router - accepts project briefs and manages the 6-skill pipeline.
"""
import uuid
import asyncio
import json
import shutil
import zipfile
import os
from datetime import datetime
from typing import Optional
from pathlib import Path
from pydantic import BaseModel
from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse, JSONResponse

from app.services.code_generator import parse_brief, generate_project
from app.services.github_service import create_repo, push_code, get_token

router = APIRouter(tags=["orchestrator"])

# In-memory job store (replace with Redis/DB in production)
jobs = {}

WORKSPACE_ROOT = Path("/tmp/future-ready-workspaces")


class ProjectBrief(BaseModel):
    project_name: str
    brief: str
    deployment_target: str = "vercel-render"
    budget_hours: Optional[int] = None
    deadline: Optional[str] = None


class JobStatus(BaseModel):
    job_id: str
    project_name: str
    status: str
    phase: str
    progress: int
    logs: list
    artifacts: list
    created_at: str
    updated_at: str
    workspace_path: Optional[str] = None
    repo_url: Optional[str] = None


@router.post("/jobs", response_model=JobStatus)
async def create_job(brief: ProjectBrief, background_tasks: BackgroundTasks):
    """Submit a new project brief and start the build pipeline."""
    job_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()

    job = {
        "job_id": job_id,
        "project_name": brief.project_name,
        "brief": brief.brief,
        "deployment_target": brief.deployment_target,
        "status": "pending",
        "phase": "initialized",
        "progress": 0,
        "logs": [],
        "artifacts": [],
        "created_at": now,
        "updated_at": now,
        "workspace_path": None,
        "repo_url": None,
    }
    jobs[job_id] = job

    background_tasks.add_task(run_pipeline, job_id, brief)
    return JobStatus(**job)


@router.get("/jobs/{job_id}", response_model=JobStatus)
async def get_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return JobStatus(**jobs[job_id])


@router.get("/jobs")
async def list_jobs():
    return [JobStatus(**job) for job in jobs.values()]


@router.post("/jobs/{job_id}/cancel")
async def cancel_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    jobs[job_id]["status"] = "cancelled"
    jobs[job_id]["updated_at"] = datetime.utcnow().isoformat()
    return {"message": "Job cancelled"}


@router.post("/jobs/{job_id}/generate")
async def generate_code(job_id: str, background_tasks: BackgroundTasks):
    """Actually generate real code files from the brief."""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]
    job["status"] = "generating"
    job["phase"] = "code-generator: Writing files"
    job["logs"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Parsing project brief...",
        "type": "command"
    })

    spec = parse_brief(job["brief"])
    spec["project_name"] = job["project_name"]

    job["logs"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": f"Detected entities: {', '.join(spec['entities'])}",
        "type": "info"
    })
    job["logs"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": f"Tech stack: {spec['tech_stack']['backend']} + {spec['tech_stack']['frontend']} + {spec['tech_stack']['database']}",
        "type": "info"
    })

    workspace = generate_project(job_id, spec)
    job["workspace_path"] = str(workspace)
    job["status"] = "generated"
    job["phase"] = "code-generator: Complete"
    job["logs"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": f"Generated project at {workspace}",
        "type": "success"
    })

    # Count files
    file_count = len([f for f in workspace.rglob("*") if f.is_file()])
    job["logs"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": f"Total files generated: {file_count}",
        "type": "success"
    })

    return {
        "job_id": job_id,
        "status": job["status"],
        "workspace": str(workspace),
        "file_count": file_count,
        "spec": spec,
    }


@router.post("/jobs/{job_id}/github")
async def push_to_github(job_id: str):
    """Create a GitHub repo and push generated code."""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]
    if not job.get("workspace_path"):
        raise HTTPException(status_code=400, detail="Code not generated yet. Call /generate first.")

    token = get_token()
    if not token:
        raise HTTPException(status_code=500, detail="No GitHub token configured")

    job["status"] = "pushing"
    job["phase"] = "github: Creating repo"
    job["logs"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Creating GitHub repository...",
        "type": "command"
    })

    try:
        repo = create_repo(
            project_name=job["project_name"],
            description=f"Generated by FutureReady Orchestrator — {job['brief'][:80]}..."
        )
        job["logs"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "message": f"Repo created: {repo['url']}",
            "type": "success"
        })

        job["phase"] = "github: Pushing code"
        job["logs"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "message": "Pushing code to origin/main...",
            "type": "command"
        })

        result = push_code(Path(job["workspace_path"]), repo)
        job["repo_url"] = result["repo_url"]
        job["status"] = "published"
        job["phase"] = "github: Published"
        job["logs"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "message": f"Pushed {result['files_pushed']} files to {result['repo_url']}",
            "type": "success"
        })

        return {
            "job_id": job_id,
            "repo_url": result["repo_url"],
            "files_pushed": result["files_pushed"],
        }

    except Exception as e:
        job["status"] = "failed"
        job["logs"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "message": f"GitHub push failed: {str(e)}",
            "type": "error"
        })
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/jobs/{job_id}/download")
async def download_zip(job_id: str):
    """Download generated code as ZIP."""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]
    if not job.get("workspace_path"):
        raise HTTPException(status_code=400, detail="Code not generated yet")

    workspace = Path(job["workspace_path"])
    zip_path = WORKSPACE_ROOT / f"{job_id}.zip"

    # Create ZIP
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in workspace.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(workspace)
                zf.write(file_path, arcname)

    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename=f"{job['project_name']}.zip"
    )


async def run_pipeline(job_id: str, brief: ProjectBrief):
    """Run the 6-phase simulation pipeline."""
    job = jobs[job_id]
    job["status"] = "running"
    job["updated_at"] = datetime.utcnow().isoformat()

    phases = [
        ("requirements-analyst", "Discovery & Specification", 15),
        ("database-architect", "Foundation", 20),
        ("backend-developer", "Backend Implementation", 25),
        ("frontend-developer", "Frontend Implementation", 25),
        ("devops-engineer", "DevOps & Deployment", 10),
        ("report-generator", "Integration & Reporting", 5),
    ]

    progress_per_phase = 100 // len(phases)

    for i, (skill_name, phase_name, duration_sec) in enumerate(phases):
        job["phase"] = f"{skill_name}: {phase_name}"
        job["logs"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "message": f"Starting {skill_name}...",
            "type": "command"
        })

        steps = 5
        for step in range(steps):
            await asyncio.sleep(duration_sec / steps)
            job["progress"] = min((i * progress_per_phase) + ((step + 1) * progress_per_phase // steps), 99)
            job["logs"].append({
                "timestamp": datetime.utcnow().isoformat(),
                "message": f"{skill_name}: step {step + 1}/{steps} complete",
                "type": "info"
            })
            job["updated_at"] = datetime.utcnow().isoformat()

        job["logs"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "message": f"{skill_name} completed",
            "type": "success"
        })

    job["artifacts"] = [
        {"name": "spec.json", "path": "output/spec.json", "type": "spec"},
        {"name": "schema.sql", "path": "output/schema.sql", "type": "database"},
        {"name": "backend/", "path": "output/backend/", "type": "code"},
        {"name": "frontend/", "path": "output/frontend/", "type": "code"},
        {"name": "docker-compose.yml", "path": "output/docker-compose.yml", "type": "infra"},
        {"name": "README.md", "path": "output/README.md", "type": "docs"},
    ]
    job["progress"] = 100
    job["phase"] = "complete"
    job["status"] = "completed"
    job["updated_at"] = datetime.utcnow().isoformat()
    job["logs"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Pipeline simulation complete! Click 'Generate Real Code' to build actual files.",
        "type": "success"
    })
