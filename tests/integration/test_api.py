"""
Integration tests for API endpoints
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_item():
    """Test creating an item"""
    item_data = {"name": "Test Item", "description": "A test item", "price": 19.99}

    response = client.post("/api/v1/items", json=item_data)
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]
    assert "id" in data


def test_get_items():
    """Test getting all items"""
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_item():
    """Test getting a non-existent item"""
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404
