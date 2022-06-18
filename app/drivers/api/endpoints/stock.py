from datetime import datetime
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


@router.post("/split", response_model=Optional[entities.StockSplit])
async def create_stock_split(
    stock_split: entities.StockSplitCreated,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> Optional[entities.Stock]:
    return su.create_split(stock_split)


@router.post("/save", response_model=entities.SavedStock)
async def save_stock_split(
    saved_stock: entities.SavedStockCreated,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> Optional[entities.SavedStock]:
    return su.save_stock(saved_stock=saved_stock)


@router.delete("/save", response_model=entities.SavedStock)
async def save_stock_split(
    b_date: datetime,
    sc: str,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> Optional[entities.SavedStock]:
    return su.delete_saved_stock(b_date=b_date, sc=sc)
