import grpc
import src.protobuf.credentials.credentials_pb2 as pb2
import src.protobuf.credentials.credentials_pb2_grpc as pb2_grpc
from src.db.query_db.get_user import get_user, viebat_data_for_tests


class CredentialsService(pb2_grpc.CredentialsServiceServicer):
    def ChangeRoleUserOnAdmin(UserCredentials):
        pass
