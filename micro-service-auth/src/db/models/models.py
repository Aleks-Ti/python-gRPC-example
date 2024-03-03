from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

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
    username: Mapped[str] = mapped_column(
        sa.String(32), nullable=False, unique=True
    )
    first_name: Mapped[str] = mapped_column(
        sa.String(64), nullable=True, unique=False
    )
    last_name: Mapped[str] = mapped_column(
        sa.String(64), nullable=True, unique=False
    )
    password: Mapped[str] = mapped_column(
        sa.String(4096), nullable=False, unique=True
    )
    is_active: Mapped[bool] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )

    date_of_registration: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=False),
        nullable=False,
        unique=False,
        default=datetime.now,
    )

    is_admin = relationship(
        "AdministrativeRights", back_populates="user", uselist=False, lazy=False
    )
    accesses = relationship(
        "Accesses", back_populates="user", uselist=False, lazy=False
    )
    profile = relationship(
        "Profile", back_populates="user", uselist=False, lazy=False
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class AdministrativeRights(Base):
    __tablename__ = "administrative_rights"

    id: Mapped[int] = mapped_column(
            sa.BigInteger, primary_key=True, nullable=False, unique=True
    )
    is_admin_id: Mapped[int] = mapped_column(
        sa.ForeignKey("admin.id"), nullable=True, unique=True,
    )
    is_moderator_id: Mapped[int] = mapped_column(
        sa.ForeignKey("moderator.id"), nullable=True, unique=True,
    )
    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey("user.id"), nullable=False, unique=True,
    )

    is_admin = relationship(
        "Admin", back_populates="authorizations", uselist=False, lazy=True
    )
    is_moderator = relationship(
        "Moderator", back_populates="authorizations", uselist=False, lazy=True
    )
    user = relationship(
        "User", back_populates="is_admin", uselist=False, lazy=True
    )


class Admin(Base):
    __tablename__ = "admin"

    id: Mapped[int] = mapped_column(
            sa.BigInteger, primary_key=True, nullable=False, unique=True
    )
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=False, nullable=False, unique=False)
    date_of_request_creation: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=False),
        nullable=False,
        unique=False,
        default=datetime.now,
    )
    role_assignment_date: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=False),
        nullable=True,
        unique=False,
        default=datetime.now,
    )

    authorizations = relationship(
        "AdministrativeRights", back_populates="is_admin", uselist=False, lazy=False
    )


class Moderator(Base):
    __tablename__ = "moderator"

    id: Mapped[int] = mapped_column(
            sa.BigInteger, primary_key=True, nullable=False, unique=True
    )
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=False, nullable=False, unique=False)
    date_of_request_creation: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=False),
        nullable=False,
        unique=False,
        default=datetime.now,
    )
    role_assignment_date: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=False),
        nullable=True,
        unique=False,
        default=datetime.now,
    )

    authorizations = relationship(
        "AdministrativeRights", back_populates="is_moderator", uselist=False, lazy=False
    )


class Accesses(Base):
    __tablename__ = "accesses"

    id: Mapped[int] = mapped_column(
            sa.BigInteger, primary_key=True, nullable=False, unique=True
    )
    user_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), nullable=False, unique=True)
    access_to_content_1: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_2: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_3: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_4: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_5: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_6: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_7: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_8: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_9: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )
    access_to_content_10: Mapped[int] = mapped_column(
        sa.Boolean, default=False, nullable=False, unique=False
    )

    user = relationship(
        "User", back_populates="accesses", uselist=False, lazy=False
    )


class Profile(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(
            sa.BigInteger, primary_key=True, nullable=False, unique=True
    )
    user_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), nullable=False, unique=True)
    achievement_id: Mapped[int] = mapped_column(
        sa.ForeignKey("achievement.id"), nullable=True, unique=False
    )

    achievement = relationship("Achievement", back_populates="profile", uselist=True)
    user = relationship("User", back_populates="profile", uselist=False)


class Achievement(Base):
    __tablename__ = "achievement"

    id: Mapped[int] = mapped_column(
            sa.BigInteger, primary_key=True, nullable=False, unique=True
    )
    title: Mapped[str] = mapped_column(
        sa.String(512), nullable=False, unique=True
    )

    profile = relationship("Profile", back_populates="achievement", uselist=True)
    user = relationship("User", back_populates="profile", uselist=False)
