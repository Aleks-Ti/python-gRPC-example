import asyncio
import os
import sys
from datetime import datetime as dt
from sqlalchemy import text

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.db.db_connector import async_session_maker  # noqa


async def load_test_users() -> None:
    async with async_session_maker() as session:
        query = text(
            """
            INSERT INTO public.user (
                fullname,
                password,
                email,
                is_admin,
                is_moderator,
                is_active,
                date_at
            )
            VALUES (
                :fullname,
                :password,
                :email,
                :is_admin,
                :is_moderator,
                :is_active,
                :date_at
            )
        """
        )
        values = [
            {
                "fullname": "adminov",
                "email": "admin@admin.admin",
                "password": "pass",
                "is_admin": True,
                "is_moderator": True,
                "is_active": True,
                "date_at": dt.now(),
            },
            {
                "fullname": "adminov_1",
                "email": "admin_1@admin.admin",
                "password": "pass_1",
                "is_admin": True,
                "is_moderator": True,
                "is_active": True,
                "date_at": dt.now(),
            },
        ]
        print("Run script. Loads Users")
        for value in values:
            await session.execute(query, value)
            await session.commit()

    print("Test user loaded!")


if __name__ == "__main__":
    asyncio.run(load_test_users())


"""
"""
