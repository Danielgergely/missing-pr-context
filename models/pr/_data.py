import datetime
from dataclasses import dataclass

from models.pr import Message, PatchSet


@dataclass
class User:
    email: str
    name: str
    username: str


@dataclass
class Data:
    branch: str
    comments: [Message]
    commitMessage: str
    createdOn: datetime.datetime
    id: str
    lastUpdated: datetime.datetime
    number: int
    open: bool
    owner: User
    patchSets: [PatchSet | None]
    project: str
    status: str
    subject: str
    url: str
