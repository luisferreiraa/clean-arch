# domain/entities/user.py
from clean_arch.domain.entities.post import Post


class User:
    def __init__(
            self,
            username: str,
            email: str,
            full_name: str | None = None,
            disabled: bool | None = None,
            id: int | None = None,
            posts: list[Post] | None = None
    ):
        self.id = id
        self.username = username
        self.email = email
        self.full_name = full_name
        self.disabled = disabled
        self.posts = posts

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id
