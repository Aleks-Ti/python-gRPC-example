from dotenv import load_dotenv
import os
from asyncpg import connect

load_dotenv()


def get_connection_params():
    return {
        'database': os.getenv('POSTGRES_DB_NAME', None),
        'user': os.getenv('POSTGRES_USERNAME', None),
        'password': os.getenv('POSTGRES_PASSWORD', None),
        'host': os.getenv('POSTGRES_HOST', 'localhost'),
        'port': os.getenv('POSTGRES_PORT', '5432'),
    }


async def db_session():
    with await connect(**get_connection_params()) as conn:
        yield conn
