from fastapi import APIRouter
from app.models.user import UserCreate

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "success",
        "message": "Backend is healthy 🚀"
    }

@router.post("/users")
async def create_user(user: UserCreate):
    return {
        "status": "created",
        "user": user
    }