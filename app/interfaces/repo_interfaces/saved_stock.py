from datetime import date
from typing import Optional

import abc
import app.domains.entities as entities


class SavedStockRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_b_date_and_sc(self, b_date: date, sc: str) -> Optional[entities.SavedStock]:
        raise NotImplementedError

    @abc.abstractmethod
    def list_by_sc(self, sc: str) -> list[entities.SavedStock]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, saved_stock_created: entities.SavedStockCreated) -> Optional[entities.SavedStockCreated]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: int) -> Optional[entities.SavedStock]:
        raise NotImplementedError
