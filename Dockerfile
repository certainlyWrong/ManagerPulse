FROM python:3.10.13-slim

WORKDIR /app
RUN apt update && \
    pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev --no-interaction
COPY . .
EXPOSE 2000
EXPOSE 80

CMD ["poetry", "run", "server"]
