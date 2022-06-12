import datetime
from typing import Optional

from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.rdb.models as models
from app.usecases.stock_usecace import StockRepositoryInterface


class StockRepository(StockRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.model = models.Stock

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

    def get_all_sc(self) -> list[str]:
        result = self.db.query(self.model.sc).group_by(self.model.sc).all()
        return [res[0] for res in result]

    def create(self, stock_created: entities.StockCreated) -> Optional[entities.Stock]:
        stock = self.model(
            sc=stock_created.sc,
            name=stock_created.name,
            market=stock_created.market,
            industry=stock_created.industry,
            b_date=stock_created.b_date,
            opened_price=stock_created.opened_price,
            high_price=stock_created.high_price,
            low_price=stock_created.low_price,
            closed_price=stock_created.closed_price,
            volume=stock_created.volume,
            transaction_price=stock_created.transaction_price,
            market_capitalization=stock_created.market_capitalization,
            low_limit=stock_created.low_limit,
            high_limit=stock_created.high_limit,
        )
        self.db.add(stock)
        self.db.commit()
        self.db.refresh(stock)
        return entities.Stock.from_orm(stock)
