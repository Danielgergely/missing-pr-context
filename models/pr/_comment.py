from dataclasses import dataclass


@dataclass
class User:
    email: str
    name: str
    username: str


@dataclass
class Comment:
    file: str
    line: int
    message: str
    reviewer: User
