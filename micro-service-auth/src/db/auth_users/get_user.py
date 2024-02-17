from src.db import db_connector
from asyncpg import connect, Connection
import logging


async def get_user(username, password):
    conn: Connection = None
    try:
        conn = await connect(**db_connector.get_connection_params())
        query = ("""
            select * from public.user as us where us.username = $1 and us.password = $2;
        """)

        # следует использовать conn.fetch или conn.fetchrow, в зависимости от того, ожидается ли одна строка результата или несколько.
        user = await conn.fetch(query, username, password)
        return user
    except Exception as err:
        conn.close()
        logging.exception(str(err))
    finally:
        if conn:
            await conn.close()


# эксперимент надо провести будет
async def get_user_alternative(username, password):
    """Надо попробовать через конектор/генгератор"""
    conn: Connection = None
    try:
        conn = db_connector.db_session()
        query = ("""
            select * from public.user as us where us.name = %s and us.email = %s;
        """)
        user = await conn.execute(query, username, password)
        return user
    except Exception as err:
        logging.exception(str(err))
