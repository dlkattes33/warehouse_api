import random
from datetime import datetime
from app.models.temperature import TemperatureReading

def generate_temperature(zone_id: str) -> TemperatureReading:
    return TemperatureReading(
        zone_id=zone_id,
        sensor_id=f"{zone_id}-sensor-1",
        value=round(random.uniform(-20, 10), 2),
        timestamp=datetime.utcnow()
    )