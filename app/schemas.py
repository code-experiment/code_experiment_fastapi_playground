from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    complete: bool


class TodoCreate(TodoBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "title": "Buy Milk",
                "complete": False
            }
        }


class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
