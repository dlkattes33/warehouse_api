from fastapi import APIRouter, HTTPException
import httpx
import sys

print("🔥 GATEWAY ROUTER LOADED 🔥", file=sys.stderr, flush=True)


router = APIRouter()

TEMPERATURE_SERVICE_URL = "http://temperature_service:8001/temperatures"

@router.get("/{zone_id}")
async def get_temperature(zone_id: str):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{TEMPERATURE_SERVICE_URL}/{zone_id}")
            resp.raise_for_status()
            
            raw =  resp.json()

            return {
                "temperature": raw["value"],
                "zone": raw["zone_id"]
            }    
        
        except httpx.HTTPError as e:
            print("TEMP SERVICE ERROR:", repr(e), file=sys.stderr, flush=True)

            raise HTTPException(status_code=502, detail="Temperature service unavailable")
