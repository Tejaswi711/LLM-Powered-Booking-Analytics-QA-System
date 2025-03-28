from fastapi import APIRouter

router = APIRouter(tags=["Main"])

@router.get("/")
async def root():
    return {
        "message": "Booking Analytics API",
        "endpoints": [
            {"path": "/health", "methods": ["GET"]},
            {"path": "/qa/ask", "methods": ["POST"]}
        ]
    }