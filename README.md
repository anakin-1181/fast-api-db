# fast-api-dbs

## Installation

### Using pip

```sh
pip install -e .
```

### Using poetry

```sh
poetry install
```

## Running the application

The application can be started using either pip or poetry

### With pip installation

```sh
uvicorn app.main:app --reload
```

### With poetry installation

```sh
poetry run uvicorn app.main:app --reload
```

### Development Server Details

- The server runs on `http://localhost:8000`
- API documentation available at: `http://localhost:8000/docs`
- Hot reload is enabled with the `--reload` flag

## Debugging with Docker

### Setup

1. Start the debug container:

```sh
docker compose -f docker-compose.debug.yml up -d
```

2. In VS Code:
   - Open the "Run and Debug" view (Ctrl+Shift+D)
   - Select "Python: Remote Attach" from the dropdown
   - Click the green play button or press F5 to start debugging

### Cleanup

After finishing your debug session:

1. Stop the container:

```sh
docker compose -f docker-compose.debug.yml down
```

2. Remove the debug container:

```sh
docker rm fastapidb-dev
```

**Note:** Always clean up the debug container before starting a new debug session to avoid port conflicts.

### Debugging Features

- Breakpoints can be set directly in VS Code
- Full debugging capabilities through `debugpy`
- Hot reloading enabled with `--reload` flag
- Debug port mapped to 5678
