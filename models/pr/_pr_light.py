import datetime
from dataclasses import dataclass

from models.bug import User
from models.pr import PatchSet


@dataclass
class PullRequestLight:
    category: str
    timestamp: datetime.datetime
    updated_on: datetime.datetime
    created_on: datetime.datetime
    commitMessage: str
    lastUpdated: datetime.datetime
    number: int
    open: bool
    owner: User
    project: str
    status: str
    subject: str
    processingTime: int | None  # in hours
    approvedBy: User | None
    approvedTime: datetime.datetime
    commitLineCount: int
    bugLinked: bool
    bugId: str | None
    bugDescription: str | None
    bugDescriptionLineCount: int | None

