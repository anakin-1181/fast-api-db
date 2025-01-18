# FastAPI Database Application

## Introduction

This is a FastAPI-based REST API application that provides CRUD (Create, Read, Update, Delete) operations for managing items in a PostgreSQL database. The application is containerized using Docker and supports both poetry and pip-based deployments.

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **PostgreSQL**: Powerful, open-source relational database
- **SQLAlchemy**: SQL toolkit and ORM for Python
- **Docker**: Containerization for consistent development and deployment
- **Pydantic**: Data validation using Python type annotations
- **pgAdmin**: Web-based PostgreSQL administration tool

## Installation

### Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose

### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd fast-api-db
```

2. Create environment file:

```bash
cp .env.sample .env
```

3. Update the .env file with your desired configuration

## Usage

### Starting the Application

The application can be started using Docker Compose with either poetry or pip profile:

#### Using Poetry (Recommended)

```bash
docker compose --profile poetry up -d
```

#### Using Pip

```bash
docker compose --profile pip up -d
```

This will start:

- FastAPI application (http://localhost:8000)
- PostgreSQL database (port 5432)
- pgAdmin interface (http://localhost:5050)

### API Endpoints

- `GET /`: Health check endpoint
- `POST /items`: Create a new item
- `GET /items/{item_id}`: Retrieve an item
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item

### API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Development

For development purposes, the application uses volume mounts to enable hot-reloading:

- `./app`: Application code
- `./src`: Source code
- PostgreSQL and pgAdmin data are persisted in Docker volumes

## Debugging

For debugging capabilities, use the debug configuration:

```bash
docker compose -f docker-compose.debug.yml up -d
```

Then connect to the debug port 5678 using your IDE's remote debugger.

### Cleanup

To stop and remove all containers:

```bash
docker compose --profile poetry/pip down
```

To remove all data volumes:

```bash
docker compose --profile poetry/pip down -v
```

## Using pgAdmin Web Interface

pgAdmin provides a web-based GUI to manage your PostgreSQL database. Access it at `http://localhost:5050`.

### Login to pgAdmin

1. Open your browser and navigate to `http://localhost:5050`
2. Login using these credentials from your `.env` file:
   - Email: `PGADMIN_DEFAULT_EMAIL`
   - Password: `PGADMIN_DEFAULT_PASSWORD`

![pgAdmin login screen](./images/image.png)

### Connect to Database Server

1. In the Dashboard, click "Add New Server"
2. Under "General" tab:

   - Name: Enter any name (e.g., "FastAPI-DB")
     ![Server creation - General tab](./images/image-1.png)

3. Under "Connection" tab:
   - Host: `pgdb` (Docker service name from docker-compose.yml)
   - Port: `5432`
   - Maintenance database: `postgres`
   - Username: `POSTGRES_USER` from .env
   - Password: `POSTGRES_PASSWORD` from .env
     ![Server creation - Connection tab](./images/image-2.png)

### Working with Database

1. Navigate through the left sidebar:

```
Servers └── Your Server └── Databases └── Your Database └── Schemas
```

2. Open Query Tool:

- Right-click your database
- Select "Query Tool"
- Write and execute SQL queries
  ![Query Tool Interface](./images/image-3.png)

### Troubleshooting

- If connection fails, ensure Docker containers are running:
  ```bash
  docker ps -a
  ```
- Check if database service is healthy:
  ```
  docker compose logs db
  ```
- Verify your `.env` credentials match between pgAdmin and PostgreSQL services
