import grpc
from src.protobuf.register import register_pb2
from src.protobuf.register import register_pb2_grpc
from src.db.query_db.get_user import register_user


class RegisterService(register_pb2_grpc.RegisterServiceServicer):
    async def RegisterUser(self, request, context):
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
