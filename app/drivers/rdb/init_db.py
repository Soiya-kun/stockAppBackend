from typing import Any

from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.interfaces as interfaces
import app.usecases as usecases


def create_user(db: Session, data: dict) -> None:
    obj_in = entities.UserCreateRequest(**data)
    repository: usecases.UserRepositoryInterface = interfaces.UserRepository(db)
    uu = usecases.UserUsecase(repository)
    uu.create(obj_in)


def create_stock(db: Session, data: dict) -> None:
    obj_in = entities.StockCreated(**data)
    repository: usecases.StockRepositoryInterface = interfaces.StockRepository(db)
    uu = usecases.StockUsecase(repository)
    uu.create(obj_in)


def init_db(db: Session, fixtures: list[dict[str, Any]]) -> None:
    for data in fixtures:
        eval(f"create_{data['model']}")(db, data["fields"])
