import datetime
from typing import Optional

import app.domains.entities as entities

from app.interfaces.repo_interfaces import (
    StockRepositoryInterface,
    ScNoteRepositoryInterface,
)
from app.interfaces.repo_interfaces import StockSplitRepositoryInterface
from app.interfaces.repo_interfaces import SavedStockRepositoryInterface


class StockUsecase:
    repo: StockRepositoryInterface
    repo_split: StockSplitRepositoryInterface
    repo_saved: SavedStockRepositoryInterface
    repo_sc_note: ScNoteRepositoryInterface

    def __init__(
        self,
        repository: StockRepositoryInterface,
        repo_split: StockSplitRepositoryInterface,
        repo_saved: SavedStockRepositoryInterface,
        repo_sc_note: ScNoteRepositoryInterface,
    ):
        self.repo: StockRepositoryInterface = repository
        self.repo_split: StockSplitRepositoryInterface = repo_split
        self.repo_saved: SavedStockRepositoryInterface = repo_saved
        self.repo_sc_note: ScNoteRepositoryInterface = repo_sc_note

    def find_by_b_date_and_sc(
        self, b_date: datetime.date, sc: str
    ) -> Optional[entities.Stock]:
        return self.repo.find_by_b_date_and_sc(b_date=b_date, sc=sc)

    def create_sc_note(self, obj_in: entities.ScNoteCreated) -> entities.ScNote:
        return self.repo_sc_note.create(obj_in=obj_in)

    def get_sc_note(self, sc: str) -> Optional[entities.ScNote]:
        return self.repo_sc_note.get_recent(sc=sc)

    def get_stocks(self, sc: str) -> list[entities.Stock]:
        ret: list[entities.Stock] = self.repo.get_stock(sc=sc)
        sss: list[entities.StockSplit] = self.repo_split.list(sc=sc)
        for ss in sss:
            for stock in ret:
                if stock.b_date <= ss.split_date:
                    stock.volume = stock.volume / ss.split_ratio
                    stock.opened_price = stock.opened_price * ss.split_ratio
                    stock.high_price = stock.high_price * ss.split_ratio
                    stock.low_price = stock.low_price * ss.split_ratio
                    stock.closed_price = stock.closed_price * ss.split_ratio
                if stock.b_date > ss.split_date:
                    break
        return ret

    def get_all_sc(self) -> list[str]:
        return self.repo.get_all_sc()

    def create(self, stock_created: entities.StockCreated) -> Optional[entities.Stock]:
        if self.find_by_b_date_and_sc(b_date=stock_created.b_date, sc=stock_created.sc):
            return None
        return self.repo.create(stock_created=stock_created)

    def create_split(
        self, stock_split_created: entities.StockSplitCreated
    ) -> Optional[entities.StockSplit]:
        if self.repo_split.find(
            sc=stock_split_created.sc, split_date=stock_split_created.split_date
        ):
            return None
        return self.repo_split.create(stock_split_created=stock_split_created)

    def save_stock(
        self, saved_stock: entities.SavedStockCreated
    ) -> Optional[entities.SavedStock]:
        stock = self.repo_saved.find_by_b_date_and_sc(
            sc=saved_stock.sc, b_date=saved_stock.b_date
        )
        if stock is not None:
            self.repo_saved.delete(id=stock.id)
        return self.repo_saved.create(saved_stock_created=saved_stock)

    def get_saved_stock_list(self, sc: str) -> list[entities.SavedStock]:
        return self.repo_saved.list_by_sc(sc=sc)

    def delete_saved_stock(self, id: int) -> Optional[entities.SavedStock]:
        return self.repo_saved.delete(id=id)

    def get_saved_stock_sc(self) -> list[str]:
        return self.repo_saved.list_of_sc()

    def get_sc_by_transaction_price(
        self, b_date: datetime.date, transaction_price: int
    ) -> list[str]:
        return self.repo.get_sc(b_date=b_date, transaction_price=transaction_price)
