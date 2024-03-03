import asyncio
import os
import sys

from sqlalchemy import text

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.db.connector_for_alembic_and_alchemy import async_session_maker  # noqa


async def load_test_users() -> None:
    async with async_session_maker() as session:
        query = text(
            """
            INSERT INTO public.user (
                name,
                fullname
            )
            VALUES (
                :name,
                :fullname
            )
        """
        )
        values = [
            {
                "name": "admin",
                "fullname": "adminov",
            },
            {
                "name": "admin1",
                "fullname": "adminov1",
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
