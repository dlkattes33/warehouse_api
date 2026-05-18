import httpx

def test_temperature_freezer():
    response = httpx.get(f"{BASE_URL}/temperatures/freezer")
    assert response.status_code == 200
    data = response.json()
    assert "value" in data
    assert "timestamp" in data
