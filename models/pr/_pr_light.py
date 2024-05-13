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

    def to_dict(self):
        return {
            "category": self.category,
            "timestamp": self.timestamp.timestamp(),
            "updated_on": self.updated_on.timestamp(),
            "created_on": self.created_on.timestamp(),
            "commitMessage": self.commitMessage,
            "lastUpdated": self.lastUpdated.timestamp(),
            "number": self.number,
            "open": self.open,
            "owner": self.owner.to_dict(),
            "project": self.project,
            "status": self.status.value,
            "subject": self.subject,
            "processingTime": self.processingTime,
            # "approvedBy": self.approvedBy.to_dict() if self.approvedBy else None,
            "approvedTime": self.approvedTime.timestamp() if self.approvedTime else None,
            "commitWordCount": self.commitWordCount,
            "bugLinked": self.bugLinked,
            "bugId": self.bugId,
            "bugDescription": self.bugDescription,
            "bugDescriptionWordCount": self.bugDescriptionWordCount,
            "iterationCount": self.iterationCount,
            "bugReopened": self.bugReopened,
            "commentCount": self.commentCount,
            "reviewCommentCount": self.reviewCommentCount
        }
