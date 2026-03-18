from pydantic import BaseModel

class InventoryUpdateRequest(BaseModel):
    item_id: str
    quantity: int

class InventoryItem(BaseModel):
    item_id: str
    quantity: int