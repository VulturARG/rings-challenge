from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Film:
    url: Optional[str] = None
    title: Optional[str] = None


@dataclass
class StarWarsCharacter:
    name: str
    films: Optional[List[Film]] = None

