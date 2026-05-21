from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LegacyLoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login-legacy")
def login_legacy(payload: LegacyLoginRequest):
    # Mock token for now
    return {"token": f"mock-token-for-{payload.username}"}
