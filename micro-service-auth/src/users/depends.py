from src.users.service import UserService
from src.users.repository import UserRepository


def user_service():
    return UserService(UserRepository)
