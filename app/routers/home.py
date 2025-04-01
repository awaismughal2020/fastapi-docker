from fastapi import APIRouter

router = APIRouter()

@router.get("/home")
def home():
    return {"message": "Hello from Home API"}
