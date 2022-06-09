import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 開発環境でTrue, 本番環境でFalse
    # OpenAPIを/docsで公開するか否かのみに利用
    DEBUG: bool = False

    # AWSの設定
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET_NAME: str

    class Config:
        env_file: str = "app/core/.env"


settings = Settings()
