import sqlalchemy as sa

from . import models
from .database import SessionLocal, engine


async def create_tables():
    # Create the database tables
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


async def reset_db():
    db = SessionLocal()
    try:
        # deleting all items and users
        await db.execute(sa.delete(models.Item))
        await db.execute(sa.delete(models.User))

        # Populate users table
        for i in range(10):
            user = models.User(
                email=f'user{i}@email.com', hashed_password=f'pwdforuser{i}'
            )
            db.add(user)
        await db.commit()

        # Populate items table
        users = (await db.execute(sa.select(models.User))).scalars().all()
        for user in users:
            for i in range(5):
                user_item = models.Item(
                    title=f'Item{i}', description=f'Item{i} description', owner=user
                )
                db.add(user_item)
        await db.commit()
    finally:
        await db.close()
