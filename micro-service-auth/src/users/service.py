from src.users.repository import UserRepository
from src.settings.exeptions import UserNotFoundEmailExeption
from src.rpc_service.utils import AuxiliaryLoginInterface


class UserService:
    def __init__(self, user_repo) -> None:
        self.user_repo: UserRepository = user_repo()

    async def login(self, user_data: AuxiliaryLoginInterface):
        user = await self.user_repo.get_user_by_email(user_data.email)
        # check pass ...
        # if pass it's OK
        # create token
        if user is None:
            raise UserNotFoundEmailExeption
        return "your_admin_token_here"
