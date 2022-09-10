import sqlalchemy as sa
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas
from .config import settings
from .dependencies import get_db
from .event_handlers import create_tables, reset_db
from .middleware import SqlTapMiddleware

app = FastAPI()

if settings.SQL_TAP:
    app.add_middleware(SqlTapMiddleware)

app.add_event_handler('startup', create_tables)
if settings.RESET_DB:
    app.add_event_handler('startup', reset_db)


@app.get('/users/', response_model=list[schemas.User])
async def read_users(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    stmt = sa.select(models.User).offset(skip).limit(limit)
    users = (await db.execute(stmt)).unique().scalars().all()
    return users
