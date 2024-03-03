from dataclasses import dataclass


@dataclass
class SearchFields:
    item_id: str
    project_name: str
    review_hash: str
