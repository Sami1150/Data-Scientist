## Run your project using cmd
```
uv venv
```

## Activate the virtual environment
```
source .venv/bin/activate
```

## Run the project
```
uv run main.py
```

## Run the unittests
```
uv run pytest -v
uv run pytest
```

## See unit test coverage

pytest tests --cov=src 