from fastapi import APIRouter
from app.models.inventory import (
    InventoryUpdateRequest,
    InventoryItem,
    InventoryCreateRequest
)
from app.services.inventory_service import (
    update_inventory,
    get_inventory_item,
    create_inventory_item,
    get_inventory_db
)

router = APIRouter()

@router.post("/update", response_model=InventoryItem)
def update_inventory_endpoint(payload: InventoryUpdateRequest):
    return update_inventory(payload)

@router.get("/{item_id}", response_model=InventoryItem)
def get_inventory_endpoint(item_id: str):
    return get_inventory_item(item_id)

@router.post("/items", response_model=InventoryItem)
def create_inventory_endpoint(payload: InventoryCreateRequest):
    item_id = f"ITEM-{len(get_inventory_db()) + 1}"
    return create_inventory_item(item_id, payload)
