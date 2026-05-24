from fastapi import APIRouter
from app.models.inventory import InventoryUpdateRequest, InventoryItem, InventoryCreateRequest
from app.services.inventory_service import update_inventory, get_inventory_item

router = APIRouter()

@router.post("/update", response_model=InventoryItem)
def update_inventory_endpoint(payload: InventoryUpdateRequest):
    return update_inventory(payload)

@router.get("/{item_id}", response_model=InventoryItem)
def get_inventory_endpoint(item_id: str):
    return get_inventory_item(item_id)

@router.post("/items", response_model=InventoryItem)
def create_inventory_item(payload: InventoryCreateRequest):
    # generate an ID (mock)
    item_id = f"ITEM-{len(inventory_db) + 1}"
    
    # Store the item in the inventory_db
    inventory_db[item_id] = {
        "name": payload.name,
        "quantity": payload.quantity,
        "location": payload.location
    }
    
    return {
        "item_id": item_id,
        "name": payload.name,
        "quantity": payload.quantity,
        "location": payload.location
    }
