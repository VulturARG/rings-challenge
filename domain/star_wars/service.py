from typing import List, Dict, Any, Optional

from domain.star_wars.dataclass import StarWarsCharacter
from domain.star_wars.repository import Repository


class StarWarService:
    """Manage star wars data."""

    def __init__(self, repository: Repository):
        self._repository = repository

    def get_api_return_description(self, name: str) -> str:
        """Get API return description."""

        characters = self._repository.get_characters()
        return self._get_fancy_description(characters)

    def _get_characters_by_name(
            self,
            name: str,
            characters: Dict[str, StarWarsCharacter]
    ) -> List[StarWarsCharacter]:
        """Find characters by name."""

        return [character for character in characters.values() if name in character.name]

    def _get_fancy_description(self, characters: Dict[str, StarWarsCharacter]) -> str:
        """Get fancy description."""

        description = ""
        for character in characters.values():
            description = self._build_phrase(description, character)

        return description

    def _build_phrase(self, description: str, character: StarWarsCharacter) -> str:
        """Build phrase."""

        if len(description) > 0 and description[-1] == ".":
            description += " "

        description += f"{character.name} participated in"

        if len(character.films) == 1:
            return description + f" {character.films[0].title}."

        for film in character.films[:len(character.films) - 1]:
            description += f" {film.title},"

        description = description[:-1]
        description += f" and {character.films[-1].title}."
        return description

