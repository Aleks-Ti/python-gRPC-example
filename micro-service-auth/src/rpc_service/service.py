import grpc
import src.protobuf.AuthService_pb2 as pb2
import src.protobuf.AuthService_pb2_grpc as pb2_grpc
from src.db.auth_users.get_user import get_user


class AuthService(pb2_grpc.AuthServiceServicer):
    async def GenerateToken(self, request, context):
        if (user := await get_user(request.username, request.password)):
            print(f"Сформирован и отправлен токен для пользователя.{user[0]['username']}")
            return pb2.TokenResponse(token="your_admin_token_here")
        else:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid username or password")
            print("Пользователь не зарегистрирован в системе.")
            return pb2.TokenResponse()
