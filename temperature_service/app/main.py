from fastapi import FastAPI
from app.routers import temperatures
from app.scheduler import temperature_scheduler
import asyncio

app = FastAPI(
    title="Temperature Service",
    version="1.0.0"
)

app.include_router(temperatures.router, prefix="/temperatures", tags=["temperatures"])

@app.on_event("startup")
async def start_scheduler():
    asyncio.create_task(temperature_scheduler())