from datetime import date
from typing import Optional

import abc
import app.domains.entities as entities


class StockRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_b_date_and_sc(self, b_date: date, sc: str) -> Optional[entities.Stock]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_stock(self, sc: str) -> list[entities.Stock]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_sc(self) -> list[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, stock_created: entities.StockCreated) -> Optional[entities.Stock]:
        raise NotImplementedError
