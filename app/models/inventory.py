from pydantic import BaseModel

class InventoryUpdateRequest(BaseModel):
    item_id: str
    name: str
    quantity: int
    location: str

class InventoryItem(BaseModel):
    item_id: str
    name: str
    quantity: int
    location: str   

class InventoryCreateRequest(BaseModel):
    name: str
    quantity: int
    location: str