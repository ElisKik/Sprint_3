class RegisteredAccount:
    """
    Object for storing credentials and real name of user.
    """

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
