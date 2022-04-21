import unittest
import requests_mock

from domain.gateway import ServerConfiguration
from domain.gateway.swapi_gateway import StarWarsURLGateway
from domain.gateway.exceptions import GatewayUnauthorized, GatewayEndpointNotFound


class TestServerGateway(unittest.TestCase):
    """Test ServerGateway class.

    Using https://requests-mock.readthedocs.io/en/latest/
    """
    
    URL = "http://url"

    def setUp(self) -> None:
        server_configuration = ServerConfiguration(
            api_root_url=self.URL, user=None, password=None,
        )
        self.star_wars_server_gateway = StarWarsURLGateway(server_configuration)

    def test_get_status_code_200(self):
        with requests_mock.Mocker() as rm:
            rm.get(self.URL, status_code=200)

            response = self.star_wars_server_gateway.get(None)
            self.assertEqual(response.status_code, 200)

    def test_get_status_code_401(self):
        with requests_mock.Mocker() as rm:
            rm.get(self.URL, status_code=401)

            with self.assertRaises(GatewayUnauthorized):
                self.star_wars_server_gateway.get(None)

    def test_get_status_code_404(self):
        with requests_mock.Mocker() as rm:
            rm.get(self.URL, status_code=404)

            with self.assertRaises(GatewayEndpointNotFound):
                self.star_wars_server_gateway.get(None)

    def test_post_status_code_200(self):
        with requests_mock.Mocker() as rm:
            rm.post(self.URL, status_code=200)

            response = self.star_wars_server_gateway.post(None)
            self.assertEqual(response.status_code, 200)

    def test_post_status_code_401(self):
        with requests_mock.Mocker() as rm:
            rm.post(self.URL, status_code=401)

            with self.assertRaises(GatewayUnauthorized):
                self.star_wars_server_gateway.post(None)

    def test_post_status_code_404(self):
        with requests_mock.Mocker() as rm:
            rm.post(self.URL, status_code=404)

            with self.assertRaises(GatewayEndpointNotFound):
                self.star_wars_server_gateway.post(None)

    def test_delete_status_code_200(self):
        with requests_mock.Mocker() as rm:
            rm.delete(self.URL, status_code=200)

            response = self.star_wars_server_gateway.delete(None)
            self.assertEqual(response.status_code, 200)

    def test_delete_status_code_401(self):
        with requests_mock.Mocker() as rm:
            rm.delete(self.URL, status_code=401)

            with self.assertRaises(GatewayUnauthorized):
                self.star_wars_server_gateway.delete(None)

    def test_delete_status_code_404(self):
        with requests_mock.Mocker() as rm:
            rm.delete(self.URL, status_code=404)

            with self.assertRaises(GatewayEndpointNotFound):
                self.star_wars_server_gateway.delete(None)
