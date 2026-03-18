from app.services.shipment_service import create_shipment, get_shipment_status
from app.models.shipment import ShipmentCreateRequest

def test_create_shipment():
    payload = ShipmentCreateRequest(item_id="A1", quantity=10, destination="NYC")
    result = create_shipment(payload)
    assert "shipment_id" in result
    assert result["status"] == "CREATED"

def test_get_shipment_status_not_found():
    result = get_shipment_status("nonexistent")
    assert result["status"] == "NOT_FOUND"