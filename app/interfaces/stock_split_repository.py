from datetime import date
from typing import Optional

from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.rdb.models as models
from app.interfaces.repo_interfaces.stock_split import StockSplitRepositoryInterface


class StockSplitRepository(StockSplitRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.model = models.StockSplit

    def create(
        self, stock_split_created: entities.StockSplitCreated
    ) -> Optional[entities.StockSplit]:
        stock_split = self.model(
            sc=stock_split_created.sc,
            split_date=stock_split_created.split_date,
            split_ratio=stock_split_created.split_ratio,
        )
        self.db.add(stock_split)
        self.db.commit()
        self.db.refresh(stock_split)
        return entities.StockSplit.from_orm(stock_split)

    def find(self, sc: str, split_date: date) -> Optional[entities.StockSplit]:
        stock_split: Optional[models.StockSplit] = (
            self.db.query(self.model)
            .filter(self.model.sc == sc, self.model.split_date == split_date)
            .first()
        )
        if stock_split is None:
            return None
        return entities.StockSplit.from_orm(stock_split)

    def list(self, sc: str) -> list[entities.StockSplit]:
        stock_splits: list[models.StockSplit] = (
            self.db.query(self.model).filter(self.model.sc == sc).all()
        )
        return [entities.StockSplit.from_orm(s) for s in stock_splits]
