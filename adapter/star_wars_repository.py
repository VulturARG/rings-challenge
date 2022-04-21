from typing import Dict, Any

from requests import Response

from domain.star_wars.dataclass import StarWarsCharacter, Film
from domain.star_wars.repository import Repository


class StarWarsRepository(Repository):

    RESULTS = "results"
    FILMS = "films"

    def __init__(self, characters: Dict[str, Any], films_titles_by_url: Dict[str, str]):
        self._characters = characters
        self._films_titles_by_url = films_titles_by_url

    def get_characters(self) -> Dict[str, StarWarsCharacter]:
        """Get the star_wars characters."""

        chars = {}

        for character in self._characters[self.RESULTS]:
            chars[character["name"]] = (
                StarWarsCharacter(
                    name=character["name"],
                    films=self._get_films(character, self._films_titles_by_url),
                )
            )
        return chars

    def _get_films(self, character, films_titles_by_url):
        return [
            Film(
                title=films_titles_by_url[film],
                url=film
            ) for film in character[self.FILMS]
        ]
