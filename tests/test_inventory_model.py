import pytest
from app.models.inventory import InventoryItem, InventoryUpdateRequest


def test_inventory_item_valid():
    item = InventoryItem(item_id="ABC123", quantity=10)
    assert item.item_id == "ABC123"
    assert item.quantity == 10


def test_inventory_update_request_valid():
    update = InventoryUpdateRequest(item_id="XYZ999", quantity=5)
    assert update.item_id == "XYZ999"
    assert update.quantity == 5


def test_inventory_item_invalid_quantity_type():
    with pytest.raises(Exception):
        InventoryItem(item_id="BAD1", quantity="not-a-number")


def test_inventory_update_request_missing_field():
    with pytest.raises(Exception):
        InventoryUpdateRequest(quantity=10)  # missing item_id


def test_inventory_item_negative_quantity_allowed():
    # If negative quantities are NOT allowed, change this test accordingly.
    item = InventoryItem(item_id="NEG1", quantity=-5)
    assert item.quantity == -5
