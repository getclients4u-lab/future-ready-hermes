from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Report, Project
from app.models.user import User
from app.services.auth import get_current_active_user

router = APIRouter()


@router.get("/")
def list_reports(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return (
        db.query(Report)
        .join(Project)
        .filter(Project.owner_id == current_user.id)
        .offset(skip)
        .limit(limit)
        .all()
    )


@router.post("/")
def create_report(
    project_id: str,
    title: str,
    format: str = "json",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    project = db.query(Project).filter(Project.id == project_id, Project.owner_id == current_user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    report = Report(project_id=project_id, title=title, format=format)
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


@router.get("/{report_id}")
def get_report(
    report_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    report = (
        db.query(Report)
        .join(Project)
        .filter(Report.id == report_id, Project.owner_id == current_user.id)
        .first()
    )
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report
