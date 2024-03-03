import datetime

from dataclasses import dataclass


@dataclass
class User:
    email: str
    name: str
    username: str


@dataclass
class Approval:
    by: User
    description: str
    grantedOn: datetime.datetime
    type: str
    value: str
