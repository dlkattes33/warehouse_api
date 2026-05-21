import pytest
from utils.client import APIClient

@pytest.fixture(scope="session")
def base_url():
    return "http://warehouse_api:8000"

@pytest.fixture(scope="session")
def client(base_url):
    return APIClient(base_url)

@pytest.fixture
def sample_inventory_item():
    return {
        "name": "Test Item",
        "quantity": 10,
        "location": "freezer"
    }

@pytest.fixture
def sample_shipment():
    return {
        "shipment_id": "SHIP-123",
        "items": [{"name": "Test Item", "quantity": 2}]
    }
