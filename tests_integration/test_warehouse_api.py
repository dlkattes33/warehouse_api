import httpx

def test_warehouse_api_root():
    response = httpx.get("http://localhost:8000/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
