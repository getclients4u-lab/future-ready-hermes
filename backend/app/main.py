from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import structlog

from app.config import settings
from app.database import engine, Base
from app.routers import auth, users, projects, reports

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up", app_name=settings.app_name)
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.create_all)
        pass
    yield
    logger.info("Shutting down")
    await engine.dispose()


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["projects"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["reports"])


@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "1.0.0"}
