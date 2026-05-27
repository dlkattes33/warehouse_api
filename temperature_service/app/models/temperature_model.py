from pydantic import BaseModel
from datetime import datetime

class TemperatureReading(BaseModel):
    zone_id: str
    sensor_id: str
    value: float
    timestamp: datetime