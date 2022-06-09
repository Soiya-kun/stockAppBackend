import os
from typing import Any

import yaml
from app.drivers.rdb.init_db import init_db
from app.drivers.rdb.base import SessionLocal


def main() -> None:
    db = SessionLocal()
    file_path = os.path.join(os.path.dirname(__file__), "init_data.yaml")
    with open(file_path, "r") as f:
        fixtures: list[dict[str, Any]] = yaml.load(f, Loader=yaml.FullLoader)

    init_db(db, fixtures)
    db.close()


if __name__ == "__main__":
    main()
