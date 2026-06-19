"""
Orchestrator router - accepts project briefs and manages the 6-skill pipeline.
"""
import uuid
import asyncio
import json
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/orchestrator", tags=["orchestrator"])

# In-memory job store (replace with Redis/DB in production)
jobs = {}


class ProjectBrief(BaseModel):
    project_name: str
    brief: str
    deployment_target: str = "vercel-render"
    budget_hours: Optional[int] = None
    deadline: Optional[str] = None


class JobStatus(BaseModel):
    job_id: str
    project_name: str
    status: str  # pending | running | completed | failed
    phase: str
    progress: int  # 0-100
    logs: list
    artifacts: list
    created_at: str
    updated_at: str


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
    }
    jobs[job_id] = job

    # Start pipeline in background
    background_tasks.add_task(run_pipeline, job_id, brief)

    return JobStatus(**job)


@router.get("/jobs/{job_id}", response_model=JobStatus)
async def get_job(job_id: str):
    """Get current status of a pipeline job."""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return JobStatus(**jobs[job_id])


@router.get("/jobs")
async def list_jobs():
    """List all pipeline jobs."""
    return [JobStatus(**job) for job in jobs.values()]


@router.post("/jobs/{job_id}/cancel")
async def cancel_job(job_id: str):
    """Cancel a running pipeline job."""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    jobs[job_id]["status"] = "cancelled"
    jobs[job_id]["updated_at"] = datetime.utcnow().isoformat()
    return {"message": "Job cancelled"}


async def run_pipeline(job_id: str, brief: ProjectBrief):
    """
    Execute the 6-phase FutureReady pipeline.
    In production, this would invoke actual skills via subprocess or API.
    """
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

        # Simulate skill execution time
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

    # Generate artifacts based on brief
    job["artifacts"] = generate_artifacts(brief)
    job["progress"] = 100
    job["phase"] = "complete"
    job["status"] = "completed"
    job["updated_at"] = datetime.utcnow().isoformat()
    job["logs"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Pipeline complete! Generated " + str(len(job["artifacts"])) + " artifacts.",
        "type": "success"
    })


def generate_artifacts(brief: ProjectBrief):
    """Generate artifact manifest based on project brief."""
    base_artifacts = [
        {"name": "spec.json", "path": "output/spec.json", "type": "spec"},
        {"name": "schema.sql", "path": "output/schema.sql", "type": "database"},
        {"name": "README.md", "path": "output/README.md", "type": "docs"},
    ]

    if "api" in brief.brief.lower() or "backend" in brief.brief.lower():
        base_artifacts.append({"name": "backend/", "path": "output/backend/", "type": "code"})

    if "frontend" in brief.brief.lower() or "ui" in brief.brief.lower() or "dashboard" in brief.brief.lower():
        base_artifacts.append({"name": "frontend/", "path": "output/frontend/", "type": "code"})

    if "docker" in brief.brief.lower() or "deploy" in brief.brief.lower():
        base_artifacts.append({"name": "docker-compose.yml", "path": "output/docker-compose.yml", "type": "infra"})

    return base_artifacts
