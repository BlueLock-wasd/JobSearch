from sqlmodel import SQLModel, Field
from sqlalchemy import BigInteger, Column
from datetime import datetime, timezone

def get_datetime():
    return datetime.now(timezone.utc)


class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: int | None = Field(
        default=None,
        sa_column=Column(BigInteger, primary_key=True)
    )
    username: str = Field(unique=True)
    password_hash: str
    created_at: datetime = Field(default_factory=get_datetime)




