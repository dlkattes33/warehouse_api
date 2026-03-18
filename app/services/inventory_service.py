inventory_db = {}

def update_inventory(payload):
    inventory_db[payload.item_id] = payload.quantity
    return {"item_id": payload.item_id, "quantity": payload.quantity}

def get_inventory_item(item_id):
    quantity = inventory_db.get(item_id, 0)
    return {"item_id": item_id, "quantity": quantity}