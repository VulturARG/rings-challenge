from typing import List, Dict, Any, Optional

from domain.star_wars.dataclass import StarWarsCharacter
from domain.star_wars.repository import StarWarsRepository


class StarWarService:
    """Manage star wars data."""

    def __init__(self, repository: StarWarsRepository):
        self._repository = repository

    def get_api_return_description(self, name: str) -> str:
        """Get API return description."""

        characters = self._repository.get_characters(name)
        wanted_characters = self._get_characters_by_name(name, characters)
        wanted_characters = self._get_films_titles_by_url(wanted_characters)
        return self._get_fancy_description(wanted_characters)

    def _get_characters_by_name(
            self,
            name: str,
            characters: Dict[str, StarWarsCharacter]
    ) -> List[StarWarsCharacter]:
        """Find characters by name."""

        return [character for character in characters.values() if name in character.name]

    def _get_films_titles_by_url(
            self,
            characters: List[StarWarsCharacter]
    ) -> List[StarWarsCharacter]:
        """Get films titles by url."""

        for character in characters:
            for film in character.films:
                film.title = self._repository.get_film_title_by_url(film.url)
        return characters

    def _get_fancy_description(self, characters: List[StarWarsCharacter]) -> str:
        """Get fancy description."""

        description = ""
        for character in characters:
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

