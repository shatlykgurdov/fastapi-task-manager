FROM python:3.12-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8001

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
CMD ["bash", "/app/start.sh"]

