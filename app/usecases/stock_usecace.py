import abc
import datetime
from typing import Optional

import app.domains.entities as entities


class StockRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_b_date_and_sc(
        self, b_date: datetime.date, sc: str
    ) -> Optional[entities.Stock]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_stock(
        self, sc: str
    ) -> list[entities.Stock]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_sc(
        self
    ) -> list[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, stock_created: entities.StockCreated) -> Optional[entities.Stock]:
        raise NotImplementedError


class StockUsecase:
    repo: StockRepositoryInterface

    def __init__(self, repository: StockRepositoryInterface):
        self.repo: StockRepositoryInterface = repository

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
