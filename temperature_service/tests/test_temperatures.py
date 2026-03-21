from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_temperature():
    response = client.get("/temperatures/freezer")
    assert response.status_code == 200
    data = response.json()
    assert data["zone_id"] == "freezer"
    assert "value" in data