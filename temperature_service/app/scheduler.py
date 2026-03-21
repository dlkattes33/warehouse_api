import asyncio
from app.services.generator import generate_temperature

ZONES = ["freezer", "cold_room", "ambient"]

async def temperature_scheduler():
    while True:
        for zone in ZONES:
            reading = generate_temperature(zone)
            # For now, just print. Later: publish to Warehouse API or Redis.
            print(f"[TEMP] {reading.zone_id}: {reading.value} C at {reading.timestamp}")
        await asyncio.sleep(5)  # run every 5 seconds