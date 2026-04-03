FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY src ./src

RUN uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:${PATH}"
ENV PORT=8000

EXPOSE 8000

CMD ["sh", "-c", "python -m azure_example_website --port ${PORT}"]