from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FutureReady API"
    debug: bool = False
    database_url: str = "postgresql+asyncpg://user:pass@localhost:5432/future_ready"
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    github_token: str = ""
    github_repo: str = ""
    cors_origins: list[str] = ["http://localhost:3000"]
    rate_limit: str = "100/minute"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
