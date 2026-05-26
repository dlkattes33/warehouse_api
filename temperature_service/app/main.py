from fastapi import FastAPI
from app.routers.temperatures import router as temperature_router
from app.scheduler import temperature_scheduler
import asyncio

app = FastAPI(
    title="Temperature Service",
    version="1.0.0"
)

app.include_router(temperature_router)

@app.on_event("startup")
async def start_scheduler():
    asyncio.create_task(temperature_scheduler())