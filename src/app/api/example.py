"""
Example API endpoints
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.example import Item, ItemCreate, ItemUpdate

router = APIRouter()

# In-memory storage (replace with database in production)
items_db = {}
item_id_counter = 1


@router.get("/items", response_model=List[Item])
async def get_items():
    """
    Get all items

    Returns:
        List[Item]: List of all items
    """
    return list(items_db.values())


@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """
    Get a specific item by ID

    Args:
        item_id: The item ID

    Returns:
        Item: The requested item

    Raises:
        HTTPException: If item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return items_db[item_id]


@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """
    Create a new item

    Args:
        item: Item data

    Returns:
        Item: The created item
    """
    global item_id_counter

    new_item = Item(
        id=item_id_counter,
        name=item.name,
        description=item.description,
        price=item.price,
    )
    items_db[item_id_counter] = new_item
    item_id_counter += 1

    return new_item


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    """
    Update an existing item

    Args:
        item_id: The item ID
        item: Updated item data

    Returns:
        Item: The updated item

    Raises:
        HTTPException: If item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    stored_item = items_db[item_id]
    update_data = item.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(stored_item, field, value)

    return stored_item


@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """
    Delete an item

    Args:
        item_id: The item ID

    Raises:
        HTTPException: If item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    del items_db[item_id]
