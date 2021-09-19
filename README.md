# migraine-diary-server

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

###数据库迁移
```shell
alembic revision --autogenerate -m "message"
alembic upgrade head
```