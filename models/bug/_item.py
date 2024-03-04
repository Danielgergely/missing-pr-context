from dataclasses import dataclass
from datetime import datetime


@dataclass
class Item:
    field: str
    fieldType: str
    from_: datetime
    fromString: str
    to: datetime
    toString: str
