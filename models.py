from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from sqlalchemy import BigInteger, Column

class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: int | None = Field(
        default=None,
        sa_column=Column(BigInteger, primary_key=True)
    )
    username: str
    is_active: bool = True

