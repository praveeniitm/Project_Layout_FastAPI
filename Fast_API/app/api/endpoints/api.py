import uvicorn
from fastapi import APIRouter

from app.api.endpoints import health_check
from app.api.endpoints import endpoints1

api_router = APIRouter()
api_router.include_router(health_check.router, prefix="health", tags=["API health check"])
api_router.include_router(endpoints1.router, prefix="/endpoints_path", tags=["endpoints tags"])
