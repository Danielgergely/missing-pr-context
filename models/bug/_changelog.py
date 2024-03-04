from dataclasses import dataclass

from models.bug import History


@dataclass
class Changelog:
    startAt: int
    maxResults: int
    total: int
    histories: [History]
