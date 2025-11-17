"""
Example business logic service
"""

from typing import List, Optional
from loguru import logger


class ExampleService:
    """
    Example service for business logic
    """

    def __init__(self):
        """Initialize the service"""
        logger.info("Example service initialized")

    async def process_data(self, data: dict) -> dict:
        """
        Process some data

        Args:
            data: Input data

        Returns:
            dict: Processed data
        """
        logger.info(f"Processing data: {data}")

        # Add your business logic here
        processed = {"original": data, "processed": True, "result": "success"}

        return processed

    async def validate_input(self, value: str) -> bool:
        """
        Validate input

        Args:
            value: Input value to validate

        Returns:
            bool: True if valid, False otherwise
        """
        # Add validation logic here
        return bool(value and len(value) > 0)


# Global service instance
example_service = ExampleService()
