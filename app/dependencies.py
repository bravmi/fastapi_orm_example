from sqlalchemy.ext.asyncio import AsyncSession

from .database import SessionLocal


async def get_db() -> AsyncSession:
    db_session: AsyncSession = SessionLocal()
    try:
        yield db_session
    except BaseException:
        await db_session.rollback()
        raise
    else:
        await db_session.commit()
    finally:
        await db_session.close()
