from fastapi import APIRouter

from app.drivers.api.endpoints import auth, stock

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/api/auth", tags=["auth"])
api_router.include_router(stock.router, prefix="/api/stock", tags=["stock"])
