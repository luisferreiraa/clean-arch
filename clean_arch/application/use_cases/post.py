# application/use_cases/post.py

from clean_arch.domain.entities.post import Post
from clean_arch.domain.exceptions.post import PostNotFoundError
from clean_arch.domain.exceptions.user import UserNotFoundError
from clean_arch.application.repositories.interfaces.post import IPostRepository


class CreatePost:
    def __init__(self, post_repo: IPostRepository):
        self.post_repo = post_repo

    def execute(self, post: Post) -> Post:
        return self.post_repo.create(post)


class GetPost:
    def __init__(self, post_repo: IPostRepository):
        self.post_repo = post_repo

    def execute(self, post_id: int) -> Post:
        post = self.post_repo.get_by_id(post_id)
        if not post:
            raise PostNotFoundError
        return post


class UpdatePost:
    def __init__(self, post_repo: IPostRepository):
        self.post_repo = post_repo

    def execute(self, post: Post) -> Post:
        existing_post = self.post_repo.get_by_id(post.id)
        if not existing_post:
            raise PostNotFoundError
        return self.post_repo.update(post)


class DeletePost:
    def __init__(self, post_repo: IPostRepository):
        self.post_repo = post_repo

    def execute(self, post_id: int) -> None:
        post = self.post_repo.get_by_id(post_id)
        if not post:
            raise PostNotFoundError
        self.post_repo.delete(post_id)
        