from unittest import TestCase

from domain.gateway import ServerConfiguration
from domain.utils.get_mesage import StarWarsMessage
from domain.utils.wiring import ManageStarWarsWiring


class TestWiring(TestCase):
    def setUp(self) -> None:
        self.wiring = ManageStarWarsWiring.for_tests()
        self.configuration = ServerConfiguration(
            api_root_url="http://localhost:8080", user=None, password=None,
        )

    def test_resolve_instances(self):

        self.assertIsInstance(
            self.wiring.get_manage_message(), StarWarsMessage
        )
