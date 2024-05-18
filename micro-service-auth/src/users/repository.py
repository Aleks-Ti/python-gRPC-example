import logging
from datetime import datetime
from src.db.db_connector import async_session_maker
from sqlalchemy import text


class UserRepository:
    async def get_user_or_none(self, current_user_id: int):
        async with async_session_maker() as session:
            query = text("""
                select * from public.user as us
                where us.id = $1;
            """)
            user = await session.execute(query, current_user_id)
            user_data = user.fetchone()
            if user_data:
                return dict(user_data)
            else:
                return None

    async def get_user_by_email(self, email: str):
        async with async_session_maker() as session:
            query = text("""
                select * from public.user as us
                where us.email = :email;
            """)
            user = await session.execute(query, {"email": email})
            user_data = user.fetchone()
            if user_data:
                return user_data
            else:
                return None

    async def get_user_by_id(self, current_user_id: int):
        async with async_session_maker() as session:
            query = text("""
                select * from public.user as us
                where us.id = $1;
            """)
            user = await session.execute(query, current_user_id)
            user_data = user.fetchone()
            if user_data:
                return dict(user_data)
            else:
                return None

    async def register_user(self, username, email, password):
        async with async_session_maker() as session:
            query = text(
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
            user = await session.execute(query, [username, email, password, time_now])
            user_data = user.fetchone()
            return dict(user_data)
