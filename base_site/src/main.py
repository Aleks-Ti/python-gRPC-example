from fastapi import Response, FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.auth.token_logic import get_token, register_user
import logging

app = FastAPI()


class User(BaseModel):
    username: str = Field(..., examples=["admin"])
    first_name: str | None
    last_name: str | None
    email: str = Field(..., examples=["admin@admin.admin"])
    password: str = Field(..., examples=["mega_hash_password"])


@app.post("/login")
async def login(user: User, user_response: Response):
    try:
        token = await get_token(user.email, user.password)
        user_response.set_cookie(key="token", value=token)
        logging.info(token)
        return {"token": token}
    except Exception as err:
        logging.warning(str(err))
        raise HTTPException(status_code=400, detail=err)


@app.post("/register")
async def register(user: User):
    try:
        register = await register_user(user.username, user.email, user.password)
        logging.info(register)
        return {"token": register}
    except Exception as err:
        logging.warning(str(err))
        raise HTTPException(
            status_code=400,
            detail="Не удалось зарегистрироваться. Возможно емаил уже используется или"
                   " username не уникален."
            )
