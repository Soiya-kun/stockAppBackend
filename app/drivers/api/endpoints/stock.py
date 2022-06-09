from typing import Optional

from fastapi import APIRouter, Depends

import app.drivers.api.deps as deps
import app.domains.entities as entities
import app.usecases as usecases

router = APIRouter()


@router.post("/list", response_model=list[Optional[entities.Stock]])
async def create_stock_data(
    stocks: list[entities.StockCreated],
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> list[Optional[entities.Stock]]:
    return [su.create(sc) for sc in stocks]
