class EmailAlreadyExistsError(Exception):
    """Raised when a user tries to register with an existing email."""

    def __init__(
        self,
        message: str = "Email already registered."
    ):
        self.message = message
        super().__init__(self.message)