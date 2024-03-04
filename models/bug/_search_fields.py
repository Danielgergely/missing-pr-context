from dataclasses import dataclass


@dataclass
class SearchFields:
    issue_key: str
    item_id: str
    project_id: str
    project_key: str
    project_name: str
