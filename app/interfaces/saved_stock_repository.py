import datetime
from typing import Optional

from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.rdb.models as models
from app.interfaces.repo_interfaces import SavedStockRepositoryInterface


class SavedStockRepository(SavedStockRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.model = models.SavedStock

    def find_by_b_date_and_sc(
            self, b_date: datetime.date, sc: str
    ) -> Optional[entities.Stock]:
        stock: Optional[models.Stock] = (
            self.db.query(self.model)
                .filter(self.model.b_date == b_date, self.model.sc == sc)
                .first()
        )
        if stock is None:
            return None
        return entities.Stock.from_orm(stock)

    def create(self, saved_stock_created: entities.SavedStockCreated) -> Optional[entities.SavedStock]:
        stock = self.model(
            sc=saved_stock_created.sc,
            b_date=saved_stock_created.b_date,
        )
        self.db.add(stock)
        self.db.commit()
        self.db.refresh(stock)
        return entities.SavedStock.from_orm(stock)
