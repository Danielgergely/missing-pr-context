import datetime
from dataclasses import dataclass

from models.bug import User

from enum import Enum


class PRStatus(Enum):
    ABANDONED = "ABANDONED"
    DEFERRED = "DEFERRED"
    INTEGRATING = "INTEGRATING"
    MERGED = "MERGED"
    NEW = "NEW"


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
    status: PRStatus
    subject: str
    processingTime: int | None  # in hours
    approvedBy: User | None
    approvedTime: datetime.datetime
    commitWordCount: int
    bugLinked: bool
    bugId: str | None
    bugDescription: str | None
    bugDescriptionWordCount: int | None
    iterationCount: int
    bugReopened: bool | None
    commentCount: int | None
    reviewCommentCount: int | None
