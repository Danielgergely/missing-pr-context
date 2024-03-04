from dataclasses import dataclass
from datetime import datetime

from models.bug import User, Item


@dataclass
class History:
    author: User
    created: datetime
    items: [Item]