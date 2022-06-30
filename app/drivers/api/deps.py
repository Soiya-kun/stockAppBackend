from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.usecases as usecases
import app.interfaces as interfaces
import app.drivers.security as security
from app.drivers.rdb.base import SessionLocal
from app.core.config import settings
from app.interfaces.repo_interfaces import StockSplitRepositoryInterface, ScNoteRepositoryInterface
from app.interfaces.repo_interfaces import SavedStockRepositoryInterface

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"api/login/access-token/")


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_usecase(db: Session = Depends(get_db)) -> usecases.UserUsecase:
    repository: usecases.UserRepositoryInterface = interfaces.UserRepository(db)
    return usecases.UserUsecase(repository)


def get_stock_usecase(db: Session = Depends(get_db)) -> usecases.StockUsecase:
    repository: usecases.StockRepositoryInterface = interfaces.StockRepository(db)
    repository_split: StockSplitRepositoryInterface = interfaces.StockSplitRepository(
        db
    )
    repository_saved: SavedStockRepositoryInterface = interfaces.SavedStockRepository(
        db
    )
    repository_sc_note: ScNoteRepositoryInterface = interfaces.ScNoteRepository(
        db
    )
    return usecases.StockUsecase(
        repository=repository,
        repo_split=repository_split,
        repo_saved=repository_saved,
        repo_sc_note=repository_sc_note
    )


def get_current_user(
    token: str = Depends(reusable_oauth2),
    uu: usecases.UserUsecase = Depends(get_user_usecase),
) -> entities.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = entities.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = uu.find_by_id(id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
