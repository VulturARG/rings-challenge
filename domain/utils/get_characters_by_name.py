from requests import Response

from domain.gateway import ServerConfiguration
from domain.gateway.swapi_gateway import StarWarsURLGateway
from domain.star_wars.gateway_service import StarWarsGatewayService


def get_characters_by_name(base_url: str, name: str) -> Response:
    """Get characters by name for external API."""

    server_configuration = ServerConfiguration(
        api_root_url=base_url,
        user=None,
        password=None
    )
    server_gateway = StarWarsURLGateway(server_configuration)
    star_wars = StarWarsGatewayService(server_gateway)
    star_wars_characters = star_wars.get_star_wars_characters(params={'search': name})
    return star_wars_characters
