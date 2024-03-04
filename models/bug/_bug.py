from datetime import datetime
from dataclasses import dataclass

from models.bug import SearchFields, Data


@dataclass
class Bug:
    backend_name: str
    backend_version: str
    perceval_version: str
    timestamp: datetime
    origin: str
    uuid: str
    updated_on: datetime
    classified_field_filters: str | None
    category: str
    search_fields: SearchFields
    tag: str
    data: Data
