FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get -y update && apt-get install -y libzbar-dev

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir poetry==1.1.11

COPY ./poetry.lock /app/poetry.lock
COPY ./pyproject.toml /app/pyproject.toml

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /app

EXPOSE 8000
CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
