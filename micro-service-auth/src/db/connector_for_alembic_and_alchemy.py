from collections.abc import Callable
from dataclasses import dataclass
from os import getenv
import subprocess
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


@dataclass
class DataBaseConfig:
    name_db: str | None = getenv("POSTGRES_DB_NAME")
    user: str | None = getenv("POSTGRES_USERNAME")
    password: str | None = getenv("POSTGRES_PASSWORD")
    port: str | None = getenv("POSTGRES_PORT")
    host: str | None = getenv("POSTGRES_HOST")

    driver: str = "asyncpg"
    database_system = "postgresql"

    def __post_init__(self):
        required_vars = ["name_db", "user", "password", "port", "host"]
        for var in required_vars:
            if getattr(self, var) is None:
                raise ValueError(
                    f"Нет переменной {var} для коннекта БД в окружении проекта."
                )

    def build_connection_str(self) -> str:
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name_db,
        ).render_as_string(hide_password=False)


def create_metadata_engine(url: URL | str) -> AsyncEngine:
    return create_async_engine(url=url, echo=True, pool_pre_ping=True)


async_session_maker: Callable[..., AsyncSession] = sessionmaker(
    create_metadata_engine(DataBaseConfig().build_connection_str()),
    class_=AsyncSession,
    expire_on_commit=False,
)


async def migrate():
    subprocess.run("alembic upgrade head", shell=True, check=True)
