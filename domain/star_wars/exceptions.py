from typing import Optional


class StarWarsException(Exception):
    """Base class for all exceptions in this module."""

    MESSAGE: Optional[str] = None


class CharacterNotFoundError(StarWarsException):
    MESSAGE = "Character Not Found"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class CharacterNotDataError(StarWarsException):
    MESSAGE = "Character response without data"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class FilmNotDataError(StarWarsException):
    MESSAGE = "Film response without data"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)
