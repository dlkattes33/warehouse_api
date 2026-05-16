from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_inventory_item():
    # This assumes your service returns an InventoryItem for "A1"
    response = client.get("/inventory/A1")
    assert response.status_code == 200

    data = response.json()
    assert "item_id" in data
    assert "quantity" in data
    assert data["item_id"] == "A1"


def test_update_inventory_item():
    payload = {"item_id": "A1", "quantity": 50}

    response = client.post("/inventory/update", json=payload)
    assert response.status_code == 200

    updated = response.json()
    assert updated["item_id"] == "A1"
    assert updated["quantity"] == 50

    # Verify the update persisted
    check = client.get("/inventory/A1")
    assert check.json()["quantity"] == 50
