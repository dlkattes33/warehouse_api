import uuid

shipments = {}

def create_shipment(payload):
    shipment_id = str(uuid.uuid4())
    shipments[shipment_id] = "CREATED"
    return {"shipment_id": shipment_id, "status": "CREATED"}

def get_shipment_status(shipment_id):
    status = shipments.get(shipment_id, "NOT_FOUND")
    return {"shipment_id": shipment_id, "status": status}