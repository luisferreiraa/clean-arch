from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from clean_arch.application.repositories.interfaces.user import IUserRepository
from clean_arch.domain.entities.user import User
from clean_arch.domain.exceptions.user import EmailAlreadyExistsError, UserNotFoundError
from clean_arch.presentation.schemas.user import UserCreate, UserResponse, UserUpdate
from clean_arch.application.use_cases.user import CreateUser, GetUser, UpdateUser, DeleteUser
from clean_arch.infrastructure.database import get_db
from clean_arch.infrastructure.repositories.user import UserRepository

router = APIRouter(prefix='/user', tags=['users'])


def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)


@router.post('/', response_model=UserResponse)
def create_user(user: UserCreate, repo: IUserRepository = Depends(get_user_repository)):
    use_case = CreateUser(repo)
    try:
        return use_case.execute(User(**user.dict()))
    except EmailAlreadyExistsError:
        raise HTTPException(status_code=400, detail='Email already registered')


@router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, repo: IUserRepository = Depends(get_user_repository)):
    use_case = GetUser(repo)
    try:
        return use_case.execute(user_id)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail='User not found')


@router.put('/{user_id}', response_model=UserResponse)
def update_user(
        user_id: int,
        user_data: UserUpdate,
        repo: IUserRepository = Depends(get_user_repository)
):
    use_case = UpdateUser(repo)
    try:
        user_dict = user_data.dict(exclude_unset=True)
        updated_user = use_case.execute(user_id, user_dict)
        return updated_user
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail='User not found')


@router.delete('/{user_id}', status_code=204)
def delete_user(user_id: int, repo: IUserRepository = Depends(get_user_repository)):
    use_case = DeleteUser(repo)
    try:
        use_case.execute(user_id)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail='User not found')
