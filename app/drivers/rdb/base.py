from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DBSettings(BaseSettings):

    username: str = "root"
    password: str = "password"
    host: str = "mysql"
    db_name: str = "stock"


settings = DBSettings()

DATABASE: str = "mysql://%s:%s@%s/%s?charset=utf8" % (
    settings.username,
    settings.password,
    settings.host,
    settings.db_name,
)

# DBとの接続
echo: bool = False  # 実行されたSQLを表示する
ENGINE = create_engine(DATABASE, encoding="utf-8", echo=echo)

# Sessionの作成
# ORM実行時の設定。自動コミットするか、自動反映するか
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

# modelで使用する
Base = declarative_base()
