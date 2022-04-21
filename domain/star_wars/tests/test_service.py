import unittest
from unittest.mock import Mock

from domain.star_wars.dataclass import StarWarsCharacter, Film
from domain.star_wars.repository import Repository
from domain.star_wars.service import StarWarService


class ServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.char_1 = StarWarsCharacter(
            name="Luke Skywalker",
            films=[
                Film(title="A New Hope", url="https://swapi.dev/api/films/1/"),
                Film(title="The Empire Strikes Back", url="https://swapi.dev/api/films/2/"),
                Film(title="Return of the Jedi", url="https://swapi.dev/api/films/3/"),
                Film(title="Revenge of the Sith", url="https://swapi.dev/api/films/4/"),
            ],
        )

        self.char_2 = StarWarsCharacter(
            name="Anakin Skywalker",
            films=[
                Film(title="The Phantom Menace", url="https://swapi.dev/api/films/1/"),
                Film(title="Attack of the Clones", url="https://swapi.dev/api/films/2/"),
                Film(title="Revenge of the Sith", url="https://swapi.dev/api/films/4/"),
            ],
        )

        self.char_3 = StarWarsCharacter(
            name="Shmi Skywalker",
            films=[
                Film(title="The Phantom Menace", url="https://swapi.dev/api/films/1/"),
                Film(title="Attack of the Clones", url="https://swapi.dev/api/films/2/"),
            ],
        )

        self.char_4 = StarWarsCharacter(
            name="Jane Doe",
            films=[
                Film(title="Film 1", url="https://swapi.dev/api/films/10/"),
                Film(title="Film 2", url="https://swapi.dev/api/films/11/"),
            ],
        )

        self.char_5 = StarWarsCharacter(
            name="John Doe",
            films=[
                Film(title="Film 4", url="https://swapi.dev/api/films/12/"),
            ],
        )

        self.star_wars_characters = {
            "Luke Skywalker": self.char_1,
            "Anakin Skywalker": self.char_2,
            "Shmi Skywalker": self.char_3,
        }

        self.mock_repository = Mock(spec=Repository)
        self.service = StarWarService(self.mock_repository)

    def test_get_characters_by_name(self):
        expected = [self.char_1, self.char_2, self.char_3]
        actual = self.service._get_characters_by_name("Skywalker", self.star_wars_characters)
        self.assertEqual(expected, actual)

    def test_get_good_api_return_description(self):

        expected = "Luke Skywalker participated in A New Hope, The Empire Strikes Back, Return of the Jedi and Revenge of the Sith. Anakin Skywalker participated in The Phantom Menace, Attack of the Clones and Revenge of the Sith. Shmi Skywalker participated in The Phantom Menace and Attack of the Clones."
        actual = self.service._get_fancy_description(self.star_wars_characters)
        self.assertEqual(expected, actual)

    def test_get_api_return_description_one_movie(self):
        expected = "John Doe participated in Film 4."
        characters = {
            "John Doe": self.char_5,
        }

        actual = self.service._get_fancy_description(characters)
        self.assertEqual(expected, actual)

    def test_get_api_return_description_two_movies(self):
        expected = "Jane Doe participated in Film 1 and Film 2."
        characters = {
            "Jane Doe": self.char_4,
        }

        actual = self.service._get_fancy_description(characters)
        self.assertEqual(expected, actual)
