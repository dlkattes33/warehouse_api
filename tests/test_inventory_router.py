from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_inventory_item():
    # This assumes your service returns an InventoryItem for "A1"
    response = client.get("/inventory/A1")
    assert response.status_code == 200

    data = response.json()
    assert "item_id" in data
    assert "name" in data
    assert "quantity" in data
    assert "location" in data
    assert data["item_id"] == "A1"
    assert data["name"] == "item_name"
    assert data["quantity"] == 10
    assert data["location"] == "freezer"


def test_update_inventory_item():
    payload = {"item_id": "A1", "name": "updated_item", "quantity": 50, "location": "refrigerator"}

    response = client.post("/inventory/update", json=payload)
    assert response.status_code == 200

    updated = response.json()
    assert updated["item_id"] == "A1"
    assert updated["quantity"] == 50
    assert updated["name"] == "updated_item"
    assert updated["location"] == "refrigerator"

    # Verify the update persisted
    check = client.get("/inventory/A1")
    assert check.json()["quantity"] == 50
