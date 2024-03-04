from dataclasses import dataclass

from models.bug import Fields, Changelog


@dataclass
class Data:
    expand: str
    id: str
    self: str
    fields: Fields
    renderedFields: dict
    transitions: []
    operations: dict
    changelog: Changelog
    comments_data: []
