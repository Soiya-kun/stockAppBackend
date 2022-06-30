import abc
from typing import Optional

import app.domains.entities as entities


class ScNoteRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, obj_in: entities.ScNoteCreated) -> entities.ScNote:
        raise NotImplementedError

    @abc.abstractmethod
    def get_recent(self, sc: str) -> Optional[entities.ScNote]:
        raise NotImplementedError
