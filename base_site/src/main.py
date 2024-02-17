from fastapi import Response, FastAPI, HTTPException
from pydantic import BaseModel
from src.auth.token_logic import get_token
import logging

app = FastAPI()


class User(BaseModel):
    username: str
    password: str


@app.post("/login")
async def login(user: User, user_response: Response):
    try:
        token = await get_token(user.username, user.password)
        user_response.set_cookie(token)
        logging.info(token)
        return {"token": token}
    except Exception as err:
        logging.warning(str(err._state.details))
        raise HTTPException(status_code=401, detail=err._state.details)
