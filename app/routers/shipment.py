from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_shipments():
    return {"shipments": []}

@router.get("/{shipment_id}")
def get_shipment(shipment_id: int):
    return {"shipment_id": shipment_id, "status": "in_transit"}
