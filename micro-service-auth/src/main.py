import src.protobuf.AuthService_pb2_grpc as pb2_grpc
from concurrent import futures
import asyncio
from src.rpc_service.service import AuthService
from grpc.experimental import aio


async def serve():
    server = aio.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port("[::]:8011")
    print("server start on port localhost:8011 / http://127.0.0.1:8011")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        print("Принудительное завершение программы.")
    except Exception as err:
        print("Ошибка в работе сервера: ", err)
