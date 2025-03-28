from fastapi import FastAPI
from .routers import health, qa, root  # Relative import

app = FastAPI(
    title="Booking Analytics API",
    version="1.0",
    description="API for booking analytics"
)

app.include_router(root.router)
app.include_router(health.router, prefix="/health", tags=["System"])
app.include_router(qa.router, prefix="/qa", tags=["QA"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)