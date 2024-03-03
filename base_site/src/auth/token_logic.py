import grpc

from src.protobuf.auth import auth_pb2
from src.protobuf.auth import auth_pb2_grpc
from src.protobuf.register import register_pb2
from src.protobuf.register import register_pb2_grpc
from src.settings.app_settings import GRPC_PORT


async def get_token(email, password):
    try:
        """channel = grpc.insecure_channel('localhost:8011'): Это создает канал для gRPC-соединения
        с сервером, который слушает на localhost и порту 8003. Функция insecure_channel указывает,
        что соединение не защищено, то есть оно не использует SSL/TLS."""
        channel = grpc.insecure_channel(f'localhost:{GRPC_PORT}')
        # важно при отладке указывать именно localhost, а то будет вываливаться ошибка dns и
        # прочее, из за того что обмен данных не защищен.

        """stub = pb2_grpc.AuthServiceStub(channel): Это создает клиентский stub для
        вызова методов сервера. pb2_grpc - это модуль, содержащий сгенерированный
        код для взаимодействия с gRPC-сервисом. AuthServiceStub - это класс, который предоставляет
        клиентские методы для вызова серверных методов."""
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        """Это вызывает метод GenerateToken на сервере, используя клиентский stub.
        Он передает UserCredentials (емаил и пароль) и ожидает ответа от сервера."""
        response = stub.LoginUser(auth_pb2.UserCredentials(email=email, password=password))
        return response.token
    except Exception as err:
        raise err


async def register_user(username, email, password):
    try:
        """channel = grpc.insecure_channel('localhost:8011'): Это создает канал для gRPC-соединения
        с сервером, который слушает на localhost и порту 8003. Функция insecure_channel указывает,
        что соединение не защищено, то есть оно не использует SSL/TLS."""
        channel = grpc.insecure_channel(f'localhost:{GRPC_PORT}')
        # важно при отладке указывать именно localhost, а то будет вываливаться ошибка dns и
        # прочее, из за того что обмен данных не защищен.

        """stub = pb2_grpc.AuthServiceStub(channel): Это создает клиентский stub для
        вызова методов сервера. pb2_grpc - это модуль, содержащий сгенерированный
        код для взаимодействия с gRPC-сервисом. AuthServiceStub - это класс, который предоставляет
        клиентские методы для вызова серверных методов."""
        stub = register_pb2_grpc.RegisterServiceStub(channel)
        """Это вызывает метод GenerateToken на сервере, используя клиентский stub.
        Он передает UserCredentials (емаил и пароль) и ожидает ответа от сервера."""
        response = stub.RegisterUser(
            register_pb2.UserRegisterCredentials(username=username, email=email, password=password)
        )
        return response.message
    except Exception:
        raise
