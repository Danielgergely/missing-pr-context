from dataclasses import dataclass


@dataclass
class User:
    self: str
    name: str
    key: str
    avatarUrls: dict
    displayName: str
    active: bool
    timeZone: str
