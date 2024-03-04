from dataclasses import dataclass


@dataclass
class Version:
    self: str
    id: str
    description: str
    name: str
    archived: bool
    release: bool
