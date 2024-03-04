from dataclasses import dataclass
from datetime import datetime

from models.bug import IssueType, Project, Watches, Priority, Version, User, Status, Component, Votes


@dataclass
class Fields:
    issuetype: IssueType
    timespent: str | None
    project: Project
    fixVersions: [Version]
    aggregatetimespent: str | None
    resolution: str | None
    resolutiondate: datetime | None
    workratio: int
    lastViewed: str | None
    watches: Watches
    created: datetime
    priority: Priority
    labels: []
    timeestimate: str | None
    aggregatetimeoriginalestimate: str | None
    versions: [Version]
    issuelinks: []
    assignee: User
    updated: datetime
    status: Status
    components: [Component]
    timeoriginalestimate: str | None
    description: str
    aggregatetimeestimate: str | None
    summary: str
    creator: User
    subtasks: []
    reporter: User
    aggregateprogress: dict
    environment: str | None
    progress: dict
    votes: Votes
    customfields: []
