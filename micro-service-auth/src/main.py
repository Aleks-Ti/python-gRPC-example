from src.protobuf.auth import auth_pb2_grpc
from src.protobuf.register import register_pb2_grpc
from src.protobuf.credentials import credentials_pb2_grpc

from concurrent import futures
import asyncio
from src.rpc_service.auth_service import AuthService
from src.rpc_service.register_service import RegisterService
from src.rpc_service.credentials_service import CredentialsService
from grpc.experimental import aio

PORT = "8011"


async def serve():
    try:
        server = aio.server(futures.ThreadPoolExecutor(max_workers=10))
        auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
        register_pb2_grpc.add_RegisterServiceServicer_to_server(RegisterService(), server)
        credentials_pb2_grpc.add_CredentialsServiceServicer_to_server(CredentialsService(), server)
        server.add_insecure_port(f"[::]:{PORT}")
        print(f"server start on port localhost:{PORT} / http://127.0.0.1:{PORT}")
        await server.start()
        await server.wait_for_termination()
    except Exception as err:
        raise err
    finally:
        server.stop()


if __name__ == "__main__":
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        print("Принудительное завершение программы.")
    except Exception as err:
        print("Ошибка в работе сервера: ", err)
