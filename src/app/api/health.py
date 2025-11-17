"""
Health check endpoints
"""

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint

    Returns:
        dict: Health status information
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
    }


@router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint

    Returns:
        dict: Readiness status information
    """
    # Add checks for database connections, external services, etc.
    return {
        "status": "ready",
        "timestamp": datetime.utcnow().isoformat(),
    }
