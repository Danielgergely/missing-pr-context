from dataclasses import dataclass


@dataclass
class ProjectCategory:
    self: str
    id: str
    description: str
    name: str
