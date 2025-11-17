"""
Helper utility functions
"""

from datetime import datetime
from typing import Any, Dict
import hashlib
import json


def generate_id(data: str) -> str:
    """
    Generate a unique ID from a string

    Args:
        data: Input string

    Returns:
        str: Generated hash ID
    """
    return hashlib.sha256(data.encode()).hexdigest()


def current_timestamp() -> str:
    """
    Get current UTC timestamp

    Returns:
        str: ISO format timestamp
    """
    return datetime.utcnow().isoformat()


def serialize_dict(data: Dict[str, Any]) -> str:
    """
    Serialize dictionary to JSON string

    Args:
        data: Dictionary to serialize

    Returns:
        str: JSON string
    """
    return json.dumps(data, default=str)


def deserialize_dict(data: str) -> Dict[str, Any]:
    """
    Deserialize JSON string to dictionary

    Args:
        data: JSON string

    Returns:
        Dict: Deserialized dictionary
    """
    return json.loads(data)
