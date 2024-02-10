import grpc
import src.rpc.AuthService_pb2 as pb2
import src.rpc.AuthService_pb2_grpc as pb2_grpc
from fastapi import Response, FastAPI, HTTPException
from pydantic import BaseModel


async def get_token(username, password):
    try:  
        """channel = grpc.insecure_channel('localhost:8011'): Это создает канал для gRPC-соединения
        с сервером, который слушает на localhost и порту 8003. Функция insecure_channel указывает,
        что соединение не защищено, то есть оно не использует SSL/TLS."""
        channel = grpc.insecure_channel('localhost:8011')
        # важно при отладке указывать именно localhost, а то будет вываливаться ошибка dns и
        # прочее, из за того что обмен данных не защищен.

        """stub = pb2_grpc.AuthServiceStub(channel): Это создает клиентский stub для
        вызова методов сервера. pb2_grpc - это модуль, содержащий сгенерированный
        код для взаимодействия с gRPC-сервисом. AuthServiceStub - это класс, который предоставляет
        клиентские методы для вызова серверных методов."""
        stub = pb2_grpc.AuthServiceStub(channel)
        """Это вызывает метод GenerateToken на сервере, используя клиентский stub.
        Он передает UserCredentials (имя пользователя и пароль) и ожидает ответа от сервера."""
        response = stub.GenerateToken(pb2.UserCredentials(username=username, password=password))
        return response.token
    except Exception as err:
        raise err

app = FastAPI()


class User(BaseModel):
    username: str
    password: str


@app.post("/login")
async def login(user: User, user_response: Response):
    try:
        token = await get_token(user.username, user.password)
        user_response.set_cookie(token)
        print(token)
        return {"token": token}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))
