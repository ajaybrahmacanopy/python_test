"""
Logging utilities
"""

import sys
from loguru import logger
from app.core.config import settings


def setup_logging():
    """
    Configure logging for the application
    """
    # Remove default handler
    logger.remove()

    # Add console handler with custom format
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=settings.log_level,
        colorize=True,
    )

    # Add file handler for production
    if settings.app_env == "production":
        logger.add(
            "logs/app_{time:YYYY-MM-DD}.log",
            rotation="00:00",
            retention="30 days",
            level=settings.log_level,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        )

    return logger
