import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, JSON
from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default="draft")  # draft, generating, reviewing, complete, error
    owner_id = Column(String, ForeignKey("users.id"), nullable=False)
    spec = Column(JSON, nullable=True)
    artifacts = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Report(Base):
    __tablename__ = "reports"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.id"), nullable=False)
    title = Column(String, nullable=False)
    format = Column(String, default="json")  # json, pdf, html
    content = Column(Text, nullable=True)
    download_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
