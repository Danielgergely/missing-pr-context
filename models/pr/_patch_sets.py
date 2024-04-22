import datetime
from dataclasses import dataclass

from models.pr import Comment
from models.pr._approval import Approval


@dataclass
class User:
    email: str
    name: str
    username: str


@dataclass
class PatchSet:
    approvals: [Approval | None]
    author: User
    comments: [Comment | None]
    createdOn: datetime.datetime
    kind: str
    number: int
    parents: [str]
    ref: str
    revision: str
    sizeDeletions: int
    sizeInsertions: int
    uploader: User
