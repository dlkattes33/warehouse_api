def test_create_inventory_item(client, sample_inventory_item):
    response = client.post("/inventory/items", json=sample_inventory_item)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == sample_inventory_item["name"]

def test_get_inventory_items(client):
    response = client.get("/inventory/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
