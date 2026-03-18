from app.models.shipment import ShipmentStatus

def test_shipment_status_contract():
    status = ShipmentStatus(shipment_id="123", status="CREATED")
    assert status.model_dump() == {"shipment_id": "123", "status": "CREATED"}