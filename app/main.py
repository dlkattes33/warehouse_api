from fastapi import FastAPI
from app.routers import inventory, shipment

app = FastAPI(
    title="Cold Storage Warehouse API",
    version="1.0.0",
    description="Mock API for inventory and shipment operations"
)

app.include_router(inventory, prefix="/inventory", tags=["Inventory"])
app.include_router(shipment, prefix="/shipment", tags=["Shipment"])