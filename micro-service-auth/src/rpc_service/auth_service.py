import grpc
import src.protobuf.auth.auth_pb2 as pb2
import src.protobuf.auth.auth_pb2_grpc as pb2_grpc
from src.users.depends import user_service
from src.rpc_service.utils import AuxiliaryLoginInterface
from src.settings.exeptions import UserNotFoundEmailExeption, PasswordInvalidExeptions


class AuthService(pb2_grpc.AuthServiceServicer):
    def __init__(self) -> None:
        self.user_repo = user_service()

    async def LoginUser(self, request: AuxiliaryLoginInterface, context):
        print("сюда заглянули")
        try:
            user_token: str = await self.user_repo.login(request)
            print(f"Сформирован и отправлен токен для пользователя: {request.email}")
            context.set_code(grpc.StatusCode.OK)
            return pb2.TokenResponse(token=user_token)
        except UserNotFoundEmailExeption:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("The user with this email address is not recognized.")
            return pb2.TokenResponse()
        except PasswordInvalidExeptions:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Invalid password.")
            return pb2.TokenResponse()
        except Exception as err:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(err))
            return pb2.TokenResponse()
