from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, eq=True)
class ServerConfiguration:
    api_root_url: str
    user: Optional[str] = None
    password: Optional[str] = None
