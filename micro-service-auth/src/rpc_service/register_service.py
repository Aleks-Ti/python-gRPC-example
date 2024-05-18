import grpc
from src.protobuf.register import register_pb2
from src.protobuf.register import register_pb2_grpc
from src.users.service import UserService


class AuxiliaryInterface:
    """
    Simulation of values from the received service data,
    if module <register_service.proto> were module <register.py>.
    from rpc_service.register.proto import UserRegisterCredentials
    """
    username: str
    email: str
    password: str


class RegisterService(register_pb2_grpc.RegisterServiceServicer):
    async def RegisterUser(self, request: AuxiliaryInterface, context):
        try:
            print("кто то пытается зарегаться")
            user = await register_user(request.username, request.email, request.password)
            if user:
                print(user)
                print("Пользователь зарегистрирован.")
                return register_pb2.NotificationRegistrMessage(
                    message="Пользователь зарегистрирован."
                )
            else:
                context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                context.set_details("Invalid username or email")
                message = "Возможно пользователь уже зарегистрирован в системе, или username занят."
                print(message)
                return register_pb2.NotificationRegistrMessage(message=message)
        except Exception as err:
            err = err
            pass

    async def ActivateUser(UserCredentials):
        pass

    async def DeactivateUser(UserCredentials):
        pass

    async def RegisterAdmin(AdminRegisterCredentials):
        pass
