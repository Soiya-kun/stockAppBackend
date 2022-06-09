## DBマイグレーション

```shell
# マイグレーションファイルの自動作成
alembic revision --autogenerate -m "migration comment"

# マイグレーションの実行。headで最新の状態まで移行。
alembic upgrade head
```