from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./app.db'

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False},
    future=True,
    echo=True,
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
)

Base = declarative_base()
