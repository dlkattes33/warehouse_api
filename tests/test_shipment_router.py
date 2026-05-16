from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_shipments():
    response = client.get("/shipment/")
    assert response.status_code == 200

    data = response.json()
    assert "shipments" in data
    assert isinstance(data["shipments"], list)
    assert data["shipments"] == []


def test_get_shipment_valid_id():
    response = client.get("/shipment/123")
    assert response.status_code == 200

    data = response.json()
    assert data["shipment_id"] == 123
    assert data["status"] == "in_transit"


def test_get_shipment_invalid_id_string():
    # FastAPI will reject non-int path params automatically
    response = client.get("/shipment/notanumber")
    assert response.status_code == 422  # Unprocessable Entity
