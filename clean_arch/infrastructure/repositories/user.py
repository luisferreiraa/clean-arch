# infrastructure/repositories/user.py
from sqlalchemy.orm import Session, joinedload

from clean_arch.domain.entities.post import Post
from clean_arch.domain.entities.user import User
from clean_arch.application.repositories.interfaces.user import IUserRepository
from clean_arch.domain.exceptions.user import UserNotFoundError
from clean_arch.infrastructure.models.user import UserModel


class UserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    # Domain -> Infrastructure (Guardar na Base de Dados)
    def create(self, user: User) -> User:
        db_user = UserModel(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            disabled=user.disabled
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User(
            id=db_user.id,
            username=db_user.username,
            email=db_user.email,
            full_name=db_user.full_name,
            disabled=db_user.disabled
        )

    # Infrastructure -> Domain (Ler da Base de Dados)
    def get_by_id(self, user_id: int) -> User | None:
        db_user = (self.db.query(UserModel)
                   .options(joinedload(UserModel.posts))
                   .filter(UserModel.id == user_id)
                   .first())
        # print(db_user.posts)
        # print(db_user.posts[0].__dict__)
        if db_user:
            return User(
                id=db_user.id,
                username=db_user.username,
                email=db_user.email,
                full_name=db_user.full_name,
                disabled=db_user.disabled,
                posts=db_user.posts
            )
        return None

    def get_by_email(self, email: str) -> User | None:
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if db_user:
            return User(
                id=db_user.id,
                username=db_user.username,
                email=db_user.email,
                full_name=db_user.full_name,
                disabled=db_user.disabled
            )
        return None

    def update(self, user: User) -> User:
        db_user = self.db.query(UserModel).filter(UserModel.id == user.id).first()
        if db_user:
            db_user.username = user.username
            db_user.email = user.email
            db_user.full_name = user.full_name
            db_user.disabled = user.disabled
            self.db.commit()
            self.db.refresh(db_user)
            return User(
                id=db_user.id,
                username=db_user.username,
                email=db_user.email,
                full_name=db_user.full_name,
                disabled=db_user.disabled
            )
        else:
            raise UserNotFoundError()

    def delete(self, user_id: int) -> None:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        else:
            raise UserNotFoundError()
