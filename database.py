from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pydantic import Field


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
    )

    host: str = '127.0.0.1'
    debug: bool = True
    db_url: str = Field(validation_alias='DATABASE_URL')

DBS = DBSettings()

engine = create_async_engine(DBS.db_url, echo=True)
async_session = async_sessionmaker(engine)

async def get_db():
    pass # найти в документации и доделать функцию