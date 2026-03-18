from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_shipment():
    payload = {"item_id": "A1", "quantity": 5, "destination": "LA"}
    create_resp = client.post("/shipment/create", json=payload)
    assert create_resp.status_code == 200

    shipment_id = create_resp.json()["shipment_id"]

    status_resp = client.get(f"/shipment/status/{shipment_id}")
    assert status_resp.status_code == 200
    assert status_resp.json()["status"] == "CREATED"