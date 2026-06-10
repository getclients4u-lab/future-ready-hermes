from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FutureReady API"
    debug: bool = False
    database_url: str = "sqlite:///./future_ready.db"
    secret_key: str = "super-secret-change-me"
    access_token_expire_minutes: int = 30
    github_token: str = ""
    github_repo: str = "getclients4u-lab/future-ready-hermes"
    cors_origins: str = "*"

    class Config:
        env_file = ".env"


settings = Settings()
