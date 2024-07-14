import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


# load_dotenv(find_dotenv(".env"))

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

engine = create_async_engine(
    url=f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@database:5432/postgres",
    echo=True,
)


sessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)

