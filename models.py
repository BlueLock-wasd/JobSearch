from sqlmodel import SQLModel, Field
from sqlalchemy import BigInteger, Column


class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: int | None = Field(
        default=None,
        sa_column=Column(BigInteger, unique=True, primary_key=True)
    )
    username: str | None = Field()
    password_hash: str


SQLModel.metadata.create_all(DATABASE_URL)

