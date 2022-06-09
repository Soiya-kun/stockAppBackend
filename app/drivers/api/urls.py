from fastapi import APIRouter

from app.drivers.api.endpoints import login, stock

api_router = APIRouter()
api_router.include_router(login.router, prefix="/api/login", tags=["login"])
api_router.include_router(stock.router, prefix="/api/stock", tags=["stock"])
