from dataclasses import dataclass
from models.bug import ProjectCategory


@dataclass
class Project:
    self: str
    id: str
    key: str
    name: str
    projectTypeKey: str
    avatarUrls: dict
    projectCategory: ProjectCategory
