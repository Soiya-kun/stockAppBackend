from datetime import date, datetime
from typing import Optional

import abc
import app.domains.entities as entities


class SavedStockRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_b_date_and_sc(self, b_date: date, sc: str) -> Optional[entities.SavedStock]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, saved_stock_created: entities.SavedStockCreated) -> Optional[entities.SavedStockCreated]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_by_b_date_and_sc(self, b_date: datetime, sc: str) -> Optional[entities.SavedStock]:
        raise NotImplementedError
