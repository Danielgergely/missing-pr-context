from dataclasses import dataclass
from datetime import datetime

from models.bug import User, Item


@dataclass
class History:
    author: User | None
    created: datetime
    items: [Item]