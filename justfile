test:
    uv run pytest --cov --cov-report=term-missing --cov-report=html

check:
    pyrefly check src
    ruff check src

verify: test check
