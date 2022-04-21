import unittest
from unittest.mock import Mock

from domain.gateway.swapi_gateway import StarWarsURLGateway
from domain.star_wars.gateway_service import StarWarsGatewayService


class GatewayServiceTestCase(unittest.TestCase):
    def setUp(self):
        with open("../../files/characters_response.json") as file:
            self.characters_response = file.read()

        self.mock_server_gateway = Mock(spec=StarWarsURLGateway)
        self.star_wars = StarWarsGatewayService(self.mock_server_gateway)

    def test_get_star_wars_characters(self):
        # values returned by the repository
        self.mock_server_gateway.get.return_value.text = self.characters_response

        actual = self.star_wars.get_star_wars_characters(params={'search': "good name"})
        self.assertEqual(self.characters_response, actual.text)

    def test_get_star_wars_film(self):
        film_response = '{"title": "Return of the Jedi"}'
        # values returned by the repository
        self.mock_server_gateway.get.return_value.text = film_response

        actual = self.star_wars.get_star_wars_characters(params={'search': "good name"})
        self.assertEqual(film_response, actual.text)

