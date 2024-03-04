from dataclasses import dataclass

import datetime


@dataclass
class User:
    email: str
    name: str
    username: str


@dataclass
class Message:
    message: str
    reviewer: User
    timestamp: datetime.datetime
