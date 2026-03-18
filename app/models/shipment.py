from pydantic import BaseModel

class ShipmentCreateRequest(BaseModel):
    item_id: str
    quantity: int
    destination: str

class ShipmentStatus(BaseModel):
    shipment_id: str
    status: str