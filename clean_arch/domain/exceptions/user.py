# domain/exceptions/user.py

class UserNotFoundError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass
