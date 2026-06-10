from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.database import get_db
from app.services.auth import get_current_user
from app.models.user import User
from app.models.project import Project, ProjectStatus

router = APIRouter()


@router.get("/")
async def list_projects(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Project).where(Project.owner_id == current_user.id))
    return result.scalars().all()


@router.post("/")
async def create_project(
    name: str,
    description: str | None = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = Project(name=name, description=description, owner_id=current_user.id)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project


@router.get("/{project_id}")
async def get_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.owner_id == current_user.id)
    )
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
