import abc
from typing import Optional

import app.domains.entities as entities


class UserRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_id(self, id: int) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_username(self, username: str) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, obj_in: entities.UserCreateRequest) -> entities.User:
        raise NotImplementedError

    @abc.abstractmethod
    def update(
        self, id: int, obj_in: entities.UserUpdateRequest
    ) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: int) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def authenticate(self, email: str, password: str) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_access_token(self, u: entities.User) -> entities.Token:
        raise NotImplementedError


class UserUsecase:
    repo: UserRepositoryInterface

    def __init__(self, repository: UserRepositoryInterface):
        self.repo: UserRepositoryInterface = repository

    def find_by_id(self, id: int) -> Optional[entities.User]:
        return self.repo.find_by_id(id)

    def create(self, obj_in: entities.UserCreateRequest) -> Optional[entities.User]:
        return self.repo.create(obj_in)

    def update(
        self, id: int, obj_in: entities.UserUpdateRequest
    ) -> Optional[entities.User]:
        return self.repo.update(id=id, obj_in=obj_in)

    def delete(self, id: int) -> Optional[entities.User]:
        return self.repo.delete(id=id)

    def authenticate(self, username: str, password: str) -> Optional[entities.User]:
        return self.repo.authenticate(username, password)

    def get_access_token(self, username: str, password: str) -> entities.Token:
        user: Optional[entities.User] = self.authenticate(
            username=username,
            password=password,
        )
        return self.repo.get_access_token(user)
