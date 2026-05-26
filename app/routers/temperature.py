from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

TEMPERATURE_SERVICE_URL = "http://temperature_service:8001"

@router.get("/{zone_id}")
async def get_temperature(zone_id: str):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{TEMPERATURE_SERVICE_URL}/{zone_id}")
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPError:
            raise HTTPException(status_code=502, detail="Temperature service unavailable")
