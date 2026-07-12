class EmailAlreadyExistsError(Exception):
    """Raised when a user tries to register with an existing email."""

    def __init__(
        self,
        message: str = "Email already registered."
    ):
        self.message = message
        super().__init__(self.message)


class InvalidCredentialsError(Exception):
    """Raised when login credentials are invalid."""

    def __init__(
        self,
        message: str = "Invalid email or password.",
    ):
        self.message = message
        super().__init__(self.message)