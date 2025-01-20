import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fast_api_db.model.model import Base

# Find .env file
load_dotenv()
# load server details
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_local = "localhost"

# Get connection string for sqlalchemy
# docker connection string
DB_URl = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# local connection string
URl = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_local}:{DB_PORT}/{DB_NAME}"


# Connection
# Use DB_URL normally, but use URL if you want to run locally
engine = create_engine(DB_URl, echo=True)
engine.connect()
SessionLocal = sessionmaker(bind=engine)


def create_table() -> None:
    Base.metadata.create_all(bind=engine)
