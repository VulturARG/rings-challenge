from typing import List, Optional, Dict

from requests import Response

from domain.gateway.gateway import Gateway
from domain.utils.join_urls import join_urls


class StarWarsGatewayService:
    """Get the star wars data from the API."""

    TIMEOUT = 10
    API_CHARACTERS_URL = "/people/"
    API_FILM_URL = "/films/"

    def __init__(self, star_wars_gateway: Gateway):
        self._star_wars_gateway = star_wars_gateway

    def get_star_wars_characters(self, params: Dict[str, str]) -> Response:
        """Get the star wars characters from the API."""

        return self._star_wars_gateway.get(
            relative_path=self.API_CHARACTERS_URL,
            params=params,
            timeout=self.TIMEOUT
        )

    def get_star_wars_film(self, film_id: int) -> Response:
        """Get the star wars films from the API."""

        return self._star_wars_gateway.get(
            relative_path=self._join_urls_if_not_none(
                self.API_FILM_URL, str(film_id)
            ),
            timeout=self.TIMEOUT
        )

    def _join_urls_if_not_none(self, *urls: Optional[str]) -> str:
        urls_without_none: List[str] = [url for url in urls if url is not None]
        return join_urls(urls_without_none)

