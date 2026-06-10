from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.database import get_db
from app.services.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/generate")
async def generate_report(
    project_id: UUID,
    format: str = "pdf",
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Placeholder: integrate with report-generator service
    return {
        "project_id": str(project_id),
        "format": format,
        "status": "queued",
        "download_url": None,
    }


@router.get("/{report_id}")
async def get_report(
    report_id: UUID,
    current_user: User = Depends(get_current_user),
):
    # Placeholder
    return {"report_id": str(report_id), "status": "completed", "url": None}
