FROM python:3.10.13-slim

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y curl && \
    pip install poetry
RUN poetry install --no-dev

EXPOSE 2000
EXPOSE 80

CMD ["poetry", "run", "server"]
