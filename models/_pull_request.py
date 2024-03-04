import datetime

from dataclasses import dataclass

from models import Data, SearchFields


@dataclass
class PullRequest:
    backend_name: str
    backend_version: str
    category: str
    classified_fields_filtered: str | None
    data: Data
    origin: str
    perceval_version: str
    search_fields: SearchFields
    tag: str
    timestamp: datetime.datetime
    updated_on: datetime.datetime
    uuid: str
