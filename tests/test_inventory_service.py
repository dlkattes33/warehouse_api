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
    assert result["quantity"] == 0


def test_update_inventory_creates_item():
    payload = InventoryUpdateRequest(item_id="A1", quantity=10)
    result = update_inventory(payload)

    assert result["item_id"] == "A1"
    assert result["quantity"] == 10
    assert inventory_db["A1"] == 10


def test_update_inventory_overwrites_existing_item():
    # First write
    payload1 = InventoryUpdateRequest(item_id="A1", quantity=5)
    update_inventory(payload1)

    # Overwrite
    payload2 = InventoryUpdateRequest(item_id="A1", quantity=99)
    result = update_inventory(payload2)

    assert result["quantity"] == 99
    assert inventory_db["A1"] == 99


def test_get_inventory_item_after_update():
    payload = InventoryUpdateRequest(item_id="B2", quantity=42)
    update_inventory(payload)

    result = get_inventory_item("B2")
    assert result["item_id"] == "B2"
    assert result["quantity"] == 42


def test_update_inventory_negative_quantity():
    payload = InventoryUpdateRequest(item_id="NEG", quantity=-7)
    result = update_inventory(payload)

    assert result["quantity"] == -7
    assert inventory_db["NEG"] == -7
