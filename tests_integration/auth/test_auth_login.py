def test_login_legacy(client):
    payload = {"username": "legacy_user", "password": "password123"}
    response = client.post("/auth/login-legacy", json=payload)

    assert response.status_code == 200
    assert "token" in response.json()
