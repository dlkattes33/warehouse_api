from fastapi import APIRouter
from app.services.generator import generate_temperature

router = APIRouter()

@router.get("/{zone_id}")
def get_temperature(zone_id: str):
    return generate_temperature(zone_id)