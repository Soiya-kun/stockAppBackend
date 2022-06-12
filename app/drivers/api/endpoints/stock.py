from typing import Optional

from fastapi import APIRouter, Depends

import app.drivers.api.deps as deps
import app.domains.entities as entities
import app.usecases as usecases

router = APIRouter()


@router.post("/list", response_model=list[Optional[entities.Stock]])
async def create_stocks(
    stocks: list[entities.StockCreated],
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> list[Optional[entities.Stock]]:
    return [su.create(sc) for sc in stocks]


@router.get("/sc/list", response_model=list[str])
async def get_all_sc(
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> list[str]:
    return su.get_all_sc()


@router.get("/list/{sc}", response_model=list[entities.Stock])
async def get_stocks(
    sc: str,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> list[entities.Stock]:
    return su.get_stocks(sc=sc)