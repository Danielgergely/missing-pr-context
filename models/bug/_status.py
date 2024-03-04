from dataclasses import dataclass


@dataclass
class Status:
    self: str
    description: str
    iconUrl: str
    name: str
    id: str
    statusCategory: dict
