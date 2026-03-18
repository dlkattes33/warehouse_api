from fastapi import APIRouter
from app.models.shipment import ShipmentCreateRequest, ShipmentStatus
from app.services.shipment_service import create_shipment, get_shipment_status

router = APIRouter()

@router.post("/create", response_model=ShipmentStatus)
def create_shipment_endpoint(payload: ShipmentCreateRequest):
    return create_shipment(payload)

@router.get("/status/{shipment_id}", response_model=ShipmentStatus)
def shipment_status_endpoint(shipment_id: str):
    return get_shipment_status(shipment_id)