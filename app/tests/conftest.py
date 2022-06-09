import os
from typing import Any, Generator

import pytest
import yaml
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import app.domains.entities as entities
import app.interfaces as interfaces
import app.usecases as usecases
from app.drivers.api.deps import get_db
from app.drivers.rdb.base import Base
from app.drivers.rdb.init_db import init_db
from app.main import app


def load_fixtures(db: Session, path: str) -> None:
    with open(path, "r") as f:
        data: list[dict[str, Any]] = yaml.load(f, Loader=yaml.FullLoader)
        init_db(db, data)


@pytest.fixture(scope="function")
def db() -> Generator:
    # settings of test database
    try:
        TEST_SQLALCHEMY_DATABASE_URL: str = "sqlite:///./test_temp.db"
        engine = create_engine(
            TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )

        # Create test database and tables
        Base.metadata.create_all(engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        file_path: str = os.path.join(
            os.path.dirname(__file__), "fixtures", "init_data.yaml"
        )
        load_fixtures(db, file_path)

        def override_get_db() -> Generator:
            try:
                db_ = SessionLocal()
                yield db_
            finally:
                db_.close()

        app.dependency_overrides[get_db] = override_get_db
        yield db
        app.dependency_overrides[get_db] = get_db
    finally:
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def user_usecase(db: Session) -> usecases.UserUsecase:
    repository: usecases.UserRepositoryInterface = interfaces.UserRepository(db)
    return usecases.UserUsecase(repository)


@pytest.fixture(scope="function")
def user_token_header(user_usecase: usecases.UserUsecase) -> dict[str, str]:
    token: entities.Token = user_usecase.get_access_token(
        username="test", password="pass"
    )
    headers = {"Authorization": f"Bearer {token.access_token}"}
    return headers
