# domain/entities/post.py
from datetime import datetime


class Post:
    def __init__(
            self,
            author: int,
            date: datetime,
            title: str,
            content: str | None = None,
            id: int | None = None
    ):
        self.id = id
        self.author = author
        self.date = date
        self.title = title
        self.content = content
