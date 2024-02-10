import grpc
import src.rpc.AuthService_pb2 as pb2
import src.rpc.AuthService_pb2_grpc as pb2_grpc
from concurrent import futures


class AuthService(pb2_grpc.AuthServiceServicer):
    def GenerateToken(self, request, context):
        print("Событие. Удаленный вызов.")
        if request.username == "admin" and request.password == "admin_password":
            print("Сформирован и отправлен токен для пользователя.")
            return pb2.TokenResponse(token="your_admin_token_here")
        else:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid username or password")
            print("Пользователь не зарегистрирован в системе.")
            return pb2.TokenResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port("[::]:8011")
    print("server start on port localhost:8011 / http://127.0.0.1:8011")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    try:
        serve()
    except KeyboardInterrupt:
        pass
