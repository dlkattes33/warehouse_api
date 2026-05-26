def test_temperature_freezer(client):
    response = client.get("/temperatures/freezer")
    assert response.status_code == 200
    data = response.json()
    assert "temperature" in data
    assert data["zone_id"] == "freezer"
