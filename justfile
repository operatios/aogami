test *ARGS:
	uv run coverage run -m pytest tests {{ARGS}}

coverage:
	uv run coverage report
	uv run coverage html

check:
    pyrefly check src
    ruff check src

verify: test check
