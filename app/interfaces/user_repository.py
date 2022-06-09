from datetime import timedelta
from typing import Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.rdb.models as models
import app.drivers.security as security
from app.core.config import settings
from app.drivers.security import get_password_hash, verify_password
from app.usecases import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.model = models.User

    def _find_by_id(self, id: int) -> Optional[models.User]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def find_by_id(self, id: int) -> Optional[entities.User]:
        user: Optional[models.User] = self._find_by_id(id)
        if user is None:
            return None
        return entities.User.from_orm(user)

    def _find_by_username(self, username: str) -> Optional[models.User]:
        return self.db.query(self.model).filter(self.model.username == username).first()

    def find_by_username(self, username: str) -> Optional[entities.User]:
        user: Optional[models.User] = self._find_by_username(username=username)
        if user is None:
            return None
        return entities.User.from_orm(user)

    def create(self, obj_in: entities.UserCreateRequest) -> entities.User:
        user = self.model(
            hashed_password=get_password_hash(obj_in.password),
            username=obj_in.username,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return entities.User.from_orm(user)

    def update(
        self, id: int, obj_in: entities.UserUpdateRequest
    ) -> Optional[entities.User]:
        user: Optional[models.User] = self._find_by_id(id)
        obj_data = jsonable_encoder(user)
        update_data: dict[str, Any] = obj_in.dict(exclude_unset=True)
        if update_data.get("password", ""):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        for field in obj_data:
            if field in update_data:
                setattr(user, field, update_data[field])
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return entities.User.from_orm(user)

    def delete(self, id: int) -> Optional[entities.User]:
        user: Optional[models.User] = self._find_by_id(id)
        if user is None:
            return None
        self.db.delete(user)
        self.db.commit()
        return entities.User.from_orm(user)

    def authenticate(self, username: str, password: str) -> Optional[entities.User]:
        user: Optional[models.User] = self._find_by_username(username=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return entities.User.from_orm(user)

    def get_access_token(self, u: entities.User) -> entities.Token:
        access_token_expires: timedelta = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        access_token: str = security.create_access_token(
            u.id, expires_delta=access_token_expires
        )
        return entities.Token(access_token=access_token, token_type="bearer")
