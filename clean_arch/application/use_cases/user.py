# application/use_cases/user.py
from typing import Callable

from clean_arch.domain.entities.user import User
from clean_arch.domain.exceptions.user import UserNotFoundError, EmailAlreadyExistsError
from clean_arch.application.repositories.interfaces.user import IUserRepository


class CreateUser:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, user: User) -> User:
        existing_user = self.user_repo.get_by_email(user.email)

        if existing_user:
            raise EmailAlreadyExistsError()
        return self.user_repo.create(user)


class GetUser:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: int) -> User:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError()
        return user


class UpdateUser:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: int, user_data: dict) -> User:
        existing_user = self.user_repo.get_by_id(user_id)
        if not existing_user:
            raise UserNotFoundError()

        updated_user = User(
            id=user_id,
            username=user_data.get("username", existing_user.username),
            email=user_data.get("email", existing_user.email),
            full_name=user_data.get("full_name", existing_user.full_name),
            disabled=user_data.get("disabled", existing_user.disabled)
        )

        return self.user_repo.update(updated_user)


class DeleteUser:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: int) -> None:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise UserNotFoundError()

        self.user_repo.delete(user_id)
