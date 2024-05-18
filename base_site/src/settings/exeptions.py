from fastapi import HTTPException


class GrpcExeptions(HTTPException):
    def __init__(self, grpc_detail) -> None:
        super().__init__(
            status_code=400,
            detail=grpc_detail,
        )
