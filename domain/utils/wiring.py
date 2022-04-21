from unittest.mock import Mock

from domain.gateway import ServerConfiguration
from domain.gateway.swapi_gateway import StarWarsURLGateway

from domain.star_wars.gateway_service import StarWarsGatewayService
from domain.utils.get_mesage import StarWarsMessage


class ManageStarWarsWiring:
    def __init__(self, api_root_url: str):
        self._api_root_url = api_root_url

    def get_manage_message(self) -> StarWarsMessage:
        return StarWarsMessage(self._get_manage_api_gateway_service())

    def _get_manage_api_gateway_service(self) -> StarWarsGatewayService:
        return StarWarsGatewayService(self._get_api_server_gateway())

    def _get_api_server_gateway(self) -> StarWarsURLGateway:
        return StarWarsURLGateway(self._get_api_server_configuration())

    def _get_api_server_configuration(self):
        """Returns a ServerConfiguration object for the API server."""

        return ServerConfiguration(
            api_root_url=self._api_root_url,
            user=None,
            password=None
        )

    @classmethod
    def for_production(cls, api_root_url: str):
        return cls(api_root_url)

    @classmethod
    def for_tests(cls):
        return cls(Mock())

