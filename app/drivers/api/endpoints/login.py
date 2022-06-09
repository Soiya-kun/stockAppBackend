from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

import app.drivers.api.deps as deps
import app.domains.entities as entities
import app.usecases as usecases

router = APIRouter()


@router.post("/access-token", response_model=entities.Token)
async def login_access_token(
    *,
    uu: usecases.UserUsecase = Depends(deps.get_user_usecase),
    credential: OAuth2PasswordRequestForm = Depends()
) -> entities.Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    return uu.get_access_token(
        username=credential.username, password=credential.password
    )


@router.get("/me", response_model=entities.User)
def read_user_me(
    current_user: entities.User = Depends(deps.get_current_user),
) -> entities.User:
    return current_user
