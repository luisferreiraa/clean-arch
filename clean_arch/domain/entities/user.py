# domain/entities/user.py

class User:
    def __init__(
            self,
            username: str,
            email: str,
            full_name: str | None = None,
            disabled: bool | None = None,
            id: int | None = None
    ):
        self.id = id
        self.username = username
        self.email = email
        self.full_name = full_name
        self.disabled = disabled

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id
