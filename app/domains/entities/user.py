from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreateRequest(UserBase):
    password: str


class UserUpdateRequest(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
