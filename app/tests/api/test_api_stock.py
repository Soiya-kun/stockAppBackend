from typing import Any, Optional

import requests
from fastapi.testclient import TestClient
from sqlalchemy.orm import scoped_session


def test_post_stock_list(
    client: TestClient, db: scoped_session, user_token_header: dict[str, str]
) -> None:
    data = [
        {
            "sc": "testsc",
            "name": "testname",
            "market": "testmarket",
            "industry": "testindustry",
            "b_date": "2022-1-2",
            "opened_price": 1500.5,
            "high_price": 1800.5,
            "low_price": 1300.5,
            "closed_price": 1400.5,
            "volume": 1000000,
            "transaction_price": 1000000000.5,
            "market_capitalization": 100000000000000.5,
            "low_limit": 1000.5,
            "high_limit": 2000.5,
        }
    ]
    r: requests.Response = client.post(
        "/api/stock/list", headers=user_token_header, json=data
    )
    expected: list[dict[str, Any]] = [
        {
            "id": 2,
            "sc": "testsc",
            "name": "testname",
            "market": "testmarket",
            "industry": "testindustry",
            "b_date": "2022-01-02",
            "opened_price": 1500.5,
            "high_price": 1800.5,
            "low_price": 1300.5,
            "closed_price": 1400.5,
            "volume": 1000000.0,
            "transaction_price": 1000000000.5,
            "market_capitalization": 100000000000000.5,
            "low_limit": 1000.5,
            "high_limit": 2000.5,
        }
    ]
    assert r.json() == expected


def test_post_stock_list_with_already_created_data(
    client: TestClient, db: scoped_session, user_token_header: dict[str, str]
) -> None:
    data = [
        {
            "sc": "testsc",
            "name": "testname",
            "market": "testmarket",
            "industry": "testindustry",
            "b_date": "2022-1-1",
            "opened_price": 1500.5,
            "high_price": 1800.5,
            "low_price": 1300.5,
            "closed_price": 1400.5,
            "volume": 1000000,
            "transaction_price": 1000000000.5,
            "market_capitalization": 100000000000000.5,
            "low_limit": 1000.5,
            "high_limit": 2000.5,
        }
    ]
    r: requests.Response = client.post(
        "/api/stock/list", headers=user_token_header, json=data
    )
    expected: list[Optional[dict[str, Any]]] = [None]
    assert r.json() == expected
