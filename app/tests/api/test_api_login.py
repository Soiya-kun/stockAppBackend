from typing import Any

import requests
from fastapi.testclient import TestClient
from sqlalchemy.orm import scoped_session


def test_get_user(
    client: TestClient, db: scoped_session, user_token_header: dict[str, str]
) -> None:
    r: requests.Response = client.get("/api/login/me", headers=user_token_header)
    expected: dict[str, Any] = {
        "id": 1,
        "username": "test",
    }
    assert r.json() == expected
