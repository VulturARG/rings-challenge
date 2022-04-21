from typing import Dict

from adapter.star_wars_repository import StarWarsRepository
from domain.star_wars.service import StarWarService
from domain.utils.get_characters_by_name import get_characters_by_name
from domain.utils.get_film_titles_by_url import get_film_titles_by_url


def get_message(name: str, base_url: str) -> Dict[str, str]:
    characters = get_characters_by_name(base_url, name)
    films_titles = get_film_titles_by_url(base_url, characters.json())
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
