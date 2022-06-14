import abc
from datetime import date
from typing import Optional

import app.domains.entities as entities


class StockSplitRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(
        self, stock_split_created: entities.StockSplitCreated
    ) -> Optional[entities.StockSplit]:
        raise NotImplementedError

    @abc.abstractmethod
    def find(self, sc: str, split_date: date) -> Optional[entities.StockSplit]:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, sc: str) -> list[entities.StockSplit]:
        raise NotImplementedError
