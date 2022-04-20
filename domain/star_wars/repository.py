from abc import ABC, abstractmethod
from typing import Dict, Optional

from domain.star_wars.dataclass import StarWarsCharacter


class StarWarsRepository(ABC):

    @abstractmethod
    def get_characters(self, name: str) -> Dict[str, StarWarsCharacter]:
        """Get the star_wars characters."""

    @abstractmethod
    def get_film_title_by_url(self, url: str) -> Optional[str]:
        """Get the star_wars characters films titles."""
