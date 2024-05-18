from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

metadata = MetaData()


@as_declarative(metadata=metadata)
class Base:
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __allow_unmapped__ = False


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        sa.BigInteger, primary_key=True, nullable=False, unique=True
    )
    fullname: Mapped[str] = mapped_column(
        sa.String(256), nullable=True, unique=False
    )
    email: Mapped[str] = mapped_column(
        sa.String(256), nullable=True, unique=True
    )
    password: Mapped[str] = mapped_column(
        sa.String(512), nullable=False, unique=True
    )
    is_active: Mapped[bool] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    is_moderator: Mapped[bool] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    is_admin: Mapped[bool] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )

    date_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=False),
        nullable=False,
        unique=False,
        default=datetime.now,
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, fullname={self.fullname!r})"
