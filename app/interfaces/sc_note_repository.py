import datetime
from typing import Optional

from sqlalchemy import asc
from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.rdb.models as models
from app.interfaces.repo_interfaces import ScNoteRepositoryInterface


class ScNoteRepository(ScNoteRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.model = models.ScNote

    def create(self, obj_in: entities.ScNoteCreated) -> entities.ScNote:
        sc_note: models.ScNote = self.model(
            sc=obj_in.sc,
            note=obj_in.note,
            b_date=obj_in.b_date
        )
        self.db.add(sc_note)
        self.db.commit()
        sc_note = self._get_recent(sc=obj_in.sc)
        return entities.ScNote.from_orm(sc_note)

    def _get_recent(self, sc: str) -> Optional[models.ScNote]:
        return (
            self.db.query(self.model)
                .filter(self.model.sc == sc)
                .order_by(asc(self.model.created_at))
                .first()
        )

    def get_recent(self, sc: str) -> Optional[entities.ScNote]:
        sc_note: Optional[models.ScNote] = self._get_recent(sc=sc)
        if sc_note is None:
            return None
        return entities.ScNote.from_orm(sc_note)
