from typing import Dict, Any, List

from domain.gateway import ServerConfiguration
from domain.gateway.swapi_gateway import StarWarsURLGateway
from domain.star_wars.gateway_service import StarWarsGatewayService

DESCRIPTION = "description"
RESULTS = "results"
FILMS = "films"
NAME = "name"
TITLE = "title"


def get_film_id_from_url(film_url: str) -> int:
    return int(film_url.split("/")[-2])


def get_film_titles_by_url(base_url: str, characters: Dict[str, Any]) -> Dict[str, str]:
    server_configuration = ServerConfiguration(
        api_root_url=base_url,
        user=None,
        password=None
    )
    server_gateway = StarWarsURLGateway(server_configuration)
    star_wars = StarWarsGatewayService(server_gateway)

    star_wars_films_titles = {}
    for character in characters[RESULTS]:
        for film_url in character[FILMS]:
            if film_url not in star_wars_films_titles:
                response = star_wars.get_star_wars_film(get_film_id_from_url(film_url))
                film = response.json()
                star_wars_films_titles[film_url] = film[TITLE]
    return star_wars_films_titles
