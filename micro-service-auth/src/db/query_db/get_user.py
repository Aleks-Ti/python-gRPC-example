from src.db import db_connector
from asyncpg import connect, Connection
import logging
from datetime import datetime

async def get_user(email, password):
    conn: Connection = None
    try:
        conn = await connect(**db_connector.get_connection_params())
        query = ("""
            select * from public.user as us where us.email = $1 and us.password = $2;
        """)

        # следует использовать conn.fetch или conn.fetchrow, в зависимости от того, ожидается ли одна строка результата или несколько.
        user = await conn.fetch(query, email, password)
        return user
    except Exception as err:
        conn.close()
        logging.exception(str(err))
    finally:
        if conn:
            await conn.close()


async def register_user(username, email, password):
    conn: Connection = None
    conn = await connect(**db_connector.get_connection_params())
    transaction = conn.transaction()
    await transaction.start()
    try:
        query = (
            """
            insert into public.user (
                is_active, username, email, password, date_of_registration
            )
            values (
                false, $1, $2, $3, $4
            );
            """
        )
        time_now = datetime.now()
        await conn.execute(query, username, email, password, time_now)
    except Exception as err:
        await transaction.rollback()
        if not conn.is_closed():
            conn.close()
        logging.exception(str(err))
        return False
    else:
        await transaction.commit()
        if not conn.is_closed():
            conn.close()
        return True


async def get_user_alternative(username, password):
    conn: Connection = None
    try:
        async for connection in db_connector.db_session():
            conn = connection
            query = ("""
                select * from public.user as us where us.name = $1 and us.email = $1;
            """)
            # user = await conn.execute(query, username, password)
            user = await conn.execute(query, username, password)
            return user
    except Exception as err:
        logging.exception(str(err))
