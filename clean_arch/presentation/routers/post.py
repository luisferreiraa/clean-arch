# presentation/routers/post.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from clean_arch.application.repositories.interfaces.post import IPostRepository
from clean_arch.application.use_cases.post import CreatePost, GetPost
from clean_arch.domain.entities.post import Post
from clean_arch.domain.exceptions.post import PostNotFoundError
from clean_arch.infrastructure.database import get_db
from clean_arch.infrastructure.repositories.post import PostRepository
from clean_arch.presentation.schemas.post import PostResponse, PostBase

router = APIRouter(prefix='/post', tags=['posts'])


def get_post_repository(db: Session = Depends(get_db)):
    return PostRepository(db)


@router.post('/', response_model=PostResponse)
def create_post(post: PostBase, repo: IPostRepository = Depends(get_post_repository)):
    use_case = CreatePost(repo)
    return use_case.execute(Post(**post.dict()))


@router.get('/{post_id}', response_model=PostResponse)
def get_post(post_id: int, repo: IPostRepository = Depends(get_post_repository)):
    use_case = GetPost(repo)
    try:
        return use_case.execute(post_id)
    except PostNotFoundError:
        raise HTTPException(status_code=404, detail='Post not found')
