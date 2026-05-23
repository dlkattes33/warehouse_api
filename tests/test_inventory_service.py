import pytest
from app.services.inventory_service import (
    inventory_db,
    update_inventory,
    get_inventory_item
)
from app.models.inventory import InventoryUpdateRequest


def setup_function():
    # Reset the in-memory DB before each test
    inventory_db.clear()


def test_get_inventory_item_default_zero():
    result = get_inventory_item("UNKNOWN")
    assert result["item_id"] == "UNKNOWN"
    assert result["name"] == "UNKNOWN"
    assert result["quantity"] == 0
    assert result["location"] == "UNKNOWN"

def test_update_inventory_creates_item():
    payload = InventoryUpdateRequest(item_id="A1", quantity=10)
    result = update_inventory(payload)

    assert result["item_id"] == "A1"
    assert result["name"] == "new_item"
    assert result["quantity"] == 10
    assert result["location"] == "freezer"
    assert inventory_db["A1"] == 10


def test_update_inventory_overwrites_existing_item():
    # First write
    payload1 = InventoryUpdateRequest(item_id="A1", name="new_item", quantity=5, location="freezer")
    update_inventory(payload1)

    # Overwrite
    payload2 = InventoryUpdateRequest(item_id="A1", name="updated_item", quantity=99, location="warehouse")
    result = update_inventory(payload2)

    assert result["quantity"] == 99
    assert result["name"] == "updated_item"
    assert result["location"] == "warehouse"
    assert inventory_db["A1"] == 99


def test_get_inventory_item_after_update():
    payload = InventoryUpdateRequest(item_id="B2", name="updated_item", quantity=42, location="warehouse")
    update_inventory(payload)

    result = get_inventory_item("B2")
    assert result["item_id"] == "B2"
    assert result["name"] == "updated_item"
    assert result["quantity"] == 42
    assert result["location"] == "warehouse"


def test_update_inventory_negative_quantity():
    payload = InventoryUpdateRequest(item_id="NEG", name="negative_item", quantity=-7, location="freezer")
    result = update_inventory(payload)

    assert result["quantity"] == -7
    assert inventory_db["NEG"] == -7
    assert result["name"] == "negative_item"
    assert result["location"] == "freezer"
