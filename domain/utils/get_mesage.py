from typing import Dict, Any

from requests import Response

from adapter.star_wars_repository import StarWarsRepository
from domain.star_wars.exceptions import (
    CharacterNotFoundError,
    CharacterNotDataError,
    FilmNotDataError
)
from domain.star_wars.gateway_service import StarWarsGatewayService
from domain.star_wars.service import StarWarService


class StarWarsMessage:
    NOT_FOUND = "Not found"
    RESULTS = "results"
    FILMS = "films"
    TITLE = "title"

    def __init__(self, star_wars_gateway: StarWarsGatewayService):
        self._server_gateway = star_wars_gateway

    def get_message(self, name: str) -> Dict[str, str]:
        characters = self.get_characters_by_name(name)
        films_titles = self.get_film_titles_by_url(characters.json())
        star_wars_repository = StarWarsRepository(
            characters=characters.json(),
            films_titles_by_url=films_titles
        )
        star_wars_service = StarWarService(star_wars_repository)
        description = star_wars_service.get_api_return_description(name=name)

        return {
            "status": characters.status_code,
            "description": description,
        }

    def get_characters_by_name(self, name: str) -> Response:
        """Get characters by name for external API."""

        characters_response = self._server_gateway.get_star_wars_characters(params={'search': name})
        star_wars_characters = characters_response.json()
        if star_wars_characters['count'] == 0:
            raise CharacterNotFoundError()
        return characters_response

    def get_film_titles_by_url(self, characters: Dict[str, Any]) -> Dict[str, str]:
        if not self.RESULTS in characters:
            raise CharacterNotDataError()

        star_wars_films_titles = {}
        for character in characters[self.RESULTS]:
            if not self.FILMS in character:
                raise FilmNotDataError()
            for film_url in character[self.FILMS]:
                if film_url in star_wars_films_titles:
                    continue
                response = self._server_gateway.get_star_wars_film(self.get_film_id_from_url(film_url))
                film = response.json()
                if self.TITLE in film:
                    star_wars_films_titles[film_url] = film[self.TITLE]
                else:
                    star_wars_films_titles[film_url] = self.NOT_FOUND
        return star_wars_films_titles

    def get_film_id_from_url(self, film_url: str) -> int:
        return int(film_url.split("/")[-2])

