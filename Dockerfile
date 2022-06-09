FROM python:3

RUN apt-get -y update && \
  apt-get install -y default-libmysqlclient-dev && \
  apt-get autoremove -y && \
  apt-get clean

RUN pip install -U pip &&\
  pip install --no-cache-dir poetry && \
  poetry config virtualenvs.create false

COPY pyproject.toml /

RUN poetry install