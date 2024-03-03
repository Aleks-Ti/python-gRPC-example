import grpc
import src.protobuf.register.register_pb2 as pb2
import src.protobuf.register.register_pb2_grpc as pb2_grpc
from src.db.query_db.get_user import get_user, viebat_data_for_tests


class RegisterService(pb2_grpc.RegisterServiceServicer):
    def RegisterUser(UserCredentials):
        pass

    def ActivateUser(UserCredentials):
        pass

    def DeactivateUser(UserCredentials):
        pass

    def RegisterAdmin(AdminRegisterCredentials):
        pass
