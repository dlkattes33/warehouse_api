import httpx

BASE_URL = "http://temperature_service:8001"

def test_temperature_freezer():
    response = httpx.get(f"{BASE_URL}/temperatures/freezer")
    assert response.status_code == 200
    data = response.json()
    assert "value" in data
    assert "timestamp" in data
