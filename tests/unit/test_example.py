"""
Unit tests for example module
"""

import pytest
from app.models.example import Item, ItemCreate


def test_item_create():
    """Test creating an item"""
    item_data = ItemCreate(name="Test Item", description="A test item", price=19.99)

    assert item_data.name == "Test Item"
    assert item_data.description == "A test item"
    assert item_data.price == 19.99


def test_item_with_id():
    """Test item with ID"""
    item = Item(id=1, name="Test Item", description="A test item", price=19.99)

    assert item.id == 1
    assert item.name == "Test Item"


def test_item_price_validation():
    """Test that price must be positive"""
    with pytest.raises(ValueError):
        ItemCreate(name="Test Item", description="A test item", price=-10.00)
