from abc import ABC, abstractmethod
from typing import Dict, List, Any

from domain.star_wars.dataclass import StarWarsCharacter


class Repository(ABC):

    @abstractmethod
    def get_characters(self) -> Dict[str, StarWarsCharacter]:
        """Get the star_wars characters."""
