# infrastructure/repositories/post.py

from sqlalchemy.orm import Session
from clean_arch.domain.entities.post import Post
from clean_arch.application.repositories.interfaces.post import IPostRepository
from clean_arch.domain.exceptions.post import PostNotFoundError
from clean_arch.infrastructure.models.post import PostModel


class PostRepository(IPostRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, post: Post) -> Post:
        db_post = PostModel(
            title=post.title,
            content=post.content,
            author=post.author,
            date=post.date
        )
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return Post(
            id=db_post.id,
            title=db_post.title,
            content=db_post.content,
            author=db_post.author,
            date=db_post.date
        )

    def get_by_id(self, post_id: int) -> Post | None:
        db_post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if db_post:
            return Post(
                id=db_post.id,
                title=db_post.title,
                content=db_post.content,
                author=db_post.author,
                date=db_post.date
            )
        return None

    def update(self, post: Post) -> Post:
        db_post = self.db.query(PostModel).filter(PostModel.id == post.id).first()
        if db_post:
            db_post.title = post.title
            db_post.content = post.content
            db_post.author = post.author
            db_post.date = post.date
            self.db.commit()
            self.db.refresh(db_post)
            return Post(
                id=db_post.id,
                title=db_post.title,
                content=db_post.content,
                author=db_post.author,
                date=db_post.date
            )
        else:
            raise PostNotFoundError()

    def delete(self, post_id: int) -> None:
        db_post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if db_post:
            self.db.delete(db_post)
            self.db.commit()
        else:
            raise PostNotFoundError
