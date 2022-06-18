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

    def _find_by_b_date_and_sc(
            self, b_date: datetime.date, sc: str
    ) -> Optional[entities.SavedStock]:
        return (
            self.db.query(self.model)
                .filter(self.model.b_date == b_date, self.model.sc == sc)
                .first()
        )

    def find_by_b_date_and_sc(
            self, b_date: datetime.date, sc: str
    ) -> Optional[entities.SavedStock]:
        saved_stock: Optional[models.Stock] = self._find_by_b_date_and_sc(b_date=b_date, sc=sc)
        if saved_stock is None:
            return None
        return entities.SavedStock.from_orm(saved_stock)

    def create(self, saved_stock_created: entities.SavedStockCreated) -> Optional[entities.SavedStock]:
        saved_stock = self.model(
            sc=saved_stock_created.sc,
            b_date=saved_stock_created.b_date,
        )
        self.db.add(saved_stock)
        self.db.commit()
        self.db.refresh(saved_stock)
        return entities.SavedStock.from_orm(saved_stock)

    def delete_by_b_date_and_sc(self, b_date: datetime, sc: str) -> Optional[entities.SavedStock]:
        saved_stock: Optional[models.SavedStock] = self._find_by_b_date_and_sc(b_date=b_date, sc=sc)
        if saved_stock is None:
            return None
        self.db.delete(saved_stock)
        self.db.commit()
        return entities.SavedStock.from_orm(saved_stock)
