from fastapi import APIRouter
from app.models.inventory import InventoryUpdateRequest, InventoryItem
from app.services.inventory_service import update_inventory, get_inventory_item

router = APIRouter()

@router.post("/update", response_model=InventoryItem)
def update_inventory_endpoint(payload: InventoryUpdateRequest):
    return update_inventory(payload)

@router.get("/{item_id}", response_model=InventoryItem)
def get_inventory_endpoint(item_id: str):
    return get_inventory_item(item_id)