from dataclasses import dataclass


@dataclass
class Votes:
    self: str
    votes: int
    hasVoted: bool
