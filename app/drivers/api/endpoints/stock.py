from datetime import datetime, date
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


@router.get("/sc/list/{b_date}/{transaction_price}", response_model=list[str])
async def get_all_sc(
    b_date: date,
    transaction_price: int,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> list[str]:
    return su.get_sc_by_transaction_price(b_date=b_date, transaction_price=transaction_price)


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


@router.get("/save/list/{sc}", response_model=list[entities.SavedStock])
async def get_saved_stock_list(
    sc: str,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> list[entities.SavedStock]:
    return su.get_saved_stock_list(sc=sc)


@router.get("/save/sc/list", response_model=list[str])
async def get_stock_sc_list(
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> list[str]:
    return su.get_saved_stock_sc()


@router.post("/save", response_model=entities.SavedStock)
async def save_stock(
    saved_stock: entities.SavedStockCreated,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> Optional[entities.SavedStock]:
    return su.save_stock(saved_stock=saved_stock)


@router.delete("/save", response_model=entities.SavedStock)
async def delete_saved_stock(
    id: int,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> Optional[entities.SavedStock]:
    return su.delete_saved_stock(id=id)


@router.post("/note", response_model=entities.ScNote)
async def create_sc_note(
    sc_note_created: entities.ScNoteCreated,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> entities.ScNote:
    return su.create_sc_note(obj_in=sc_note_created)


@router.get("/note", response_model=entities.ScNote)
async def get_sc_note(
    sc: str,
    su: usecases.StockUsecase = Depends(deps.get_stock_usecase),
) -> Optional[entities.ScNote]:
    return su.get_sc_note(sc=sc)
