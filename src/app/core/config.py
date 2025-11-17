"""
Configuration management
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    app_name: str = "python-deployment"
    app_env: str = "development"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = int(os.getenv("PORT", "8000"))  # Railway provides PORT env var
    log_level: str = "INFO"

    # Database (optional)
    database_url: Optional[str] = None

    # Redis (optional)
    redis_url: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
