# application/repositories/interfaces/post.py
from abc import ABC, abstractmethod
from clean_arch.domain.entities.post import Post


class IPostRepository(ABC):
    @abstractmethod
    def create(self, post: Post) -> Post:
        pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Post:
        pass

    @abstractmethod
    def update(self, post: Post) -> Post:
        pass

    @abstractmethod
    def delete(self, post_id: int) -> None:
        pass
