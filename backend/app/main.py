from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine, Base
from app.routers import auth, users, projects, reports, orchestrator, build

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="AI-powered full-stack code generation platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.cors_origins == "*" else settings.cors_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["projects"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["reports"])
app.include_router(build.router, prefix="/api/v1/build", tags=["build"])
app.include_router(orchestrator.router, prefix="/api/v1/orchestrator", tags=["orchestrator"])


@app.get("/health")
def health_check():
    return {"status": "ok", "service": settings.app_name}


@app.get("/")
def root():
    return {
        "message": "FutureReady API",
        "version": "1.0.0",
        "docs": "/docs",
    }
