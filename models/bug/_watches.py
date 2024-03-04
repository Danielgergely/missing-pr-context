from dataclasses import dataclass


@dataclass
class Watches:
    self: str
    watchCount: int
    isWatching: bool
