import os

import sqlalchemy as sa
import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas
from .database import SessionLocal, engine
from .middleware import SqlTapMiddleware

app = FastAPI()

if os.environ.get('SQL_TAP') == '1':
    app.add_middleware(SqlTapMiddleware)


@app.on_event('startup')
async def create_tables():
    # Create the database tables
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


# Dependency
async def get_db() -> AsyncSession:
    try:
        db: AsyncSession = SessionLocal()
        yield db
    finally:
        await db.close()


@app.on_event('startup')
async def reset_db():
    db = SessionLocal()
    try:
        # deleting all items and users
        await db.execute(sa.delete(models.Item))
        await db.execute(sa.delete(models.User))

        # Populate users table
        for i in range(50):
            user = models.User(
                email=f'user{i}@email.com', hashed_password=f'pwdforuser{i}'
            )
            db.add(user)
        await db.commit()

        # Populate items table
        users = (await db.execute(sa.select(models.User))).scalars().all()
        for user in users:
            for i in range(20):
                user_item = models.Item(
                    title=f'Item{i}', description=f'Item{i} description', owner=user
                )
                db.add(user_item)
        await db.commit()
    finally:
        await db.close()


@app.get('/users/', response_model=list[schemas.User])
async def read_users(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    stmt = sa.select(models.User).offset(skip).limit(limit)
    users = (await db.execute(stmt)).unique().scalars().all()
    return users


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
