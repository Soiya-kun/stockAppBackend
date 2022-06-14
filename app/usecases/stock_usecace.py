
import datetime
from typing import Optional

import app.domains.entities as entities

from app.interfaces.repo_interfaces import StockRepositoryInterface
from app.interfaces.repo_interfaces import StockSplitRepositoryInterface


class StockUsecase:
    repo: StockRepositoryInterface
    repo_split: StockSplitRepositoryInterface

    def __init__(self, repository: StockRepositoryInterface, repo_split: StockSplitRepositoryInterface):
        self.repo: StockRepositoryInterface = repository
        self.repo_split: StockSplitRepositoryInterface = repo_split

    def find_by_b_date_and_sc(
        self, b_date: datetime.date, sc: str
    ) -> Optional[entities.Stock]:
        return self.repo.find_by_b_date_and_sc(b_date=b_date, sc=sc)

    def get_stocks(self, sc: str) -> list[entities.Stock]:
        return self.repo.get_stock(sc=sc)

    def get_all_sc(
            self
    ) -> list[str]:
        return self.repo.get_all_sc()

    def create(self, stock_created: entities.StockCreated) -> Optional[entities.Stock]:
        if self.find_by_b_date_and_sc(b_date=stock_created.b_date, sc=stock_created.sc):
            return None
        return self.repo.create(stock_created=stock_created)

    def create_split(self, stock_split_created: entities.StockSplitCreated) -> Optional[entities.StockSplit]:
        if self.repo_split.find(sc=stock_split_created.sc, split_date=stock_split_created.split_date):
            return None
        return self.repo_split.create(stock_split_created=stock_split_created)
