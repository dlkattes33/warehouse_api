# app/services/inventory_service.py 
inventory_db = {}

def update_inventory(payload):
    inventory_db[payload.item_id] = {"name": payload.name, "quantity": payload.quantity, "location": payload.location}
    return {"item_id": payload.item_id, "name": payload.name, "quantity": payload.quantity, "location": payload.location}

def get_inventory_item(item_id):
    item = inventory_db.get(item_id)
    if not item:
        return {"item_id": item_id, "name": "UNKNOWN", "quantity": 0, "location": "UNKNOWN"}
    return {"item_id": item_id, "name": item["name"], "quantity": item["quantity"], "location": item["location"]}