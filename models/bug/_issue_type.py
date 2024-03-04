from dataclasses import dataclass


@dataclass
class IssueType:
    self: str
    id: str
    description: str
    iconUrl: str
    name: str
    subtask: bool
    avatarId: int