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

@router.get("/items", response_model=list[InventoryItem])
def list_inventory_items():
    db = get_inventory_db()
    items = []
    for item_id, data in db.items():
        items.append({
            "item_id": item_id,
            "name": data["name"],
            "quantity": data["quantity"],
            "location": data["location"]
        })
    return items

@router.post("/items", response_model=InventoryItem)
def create_inventory_endpoint(payload: InventoryCreateRequest):
    item_id = f"ITEM-{len(get_inventory_db()) + 1}"
    return create_inventory_item(item_id, payload)

