from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    owner_id: int
    description: str | None = None

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    email: str
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
