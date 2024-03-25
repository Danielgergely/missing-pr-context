from mapper.bug import SearchFieldsMapper, DataMapper
from models.bug import Bug
from datetime import datetime


class BugMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Bug:
        return Bug(backend_name=_dict.get("backend_name"),
                   backend_version=_dict.get("backend_version"),
                   perceval_version=_dict.get("perceval_version"),
                   timestamp=datetime.fromtimestamp(_dict.get("timestamp")),
                   origin=_dict.get("origin"),
                   uuid=_dict.get("uuid"),
                   updated_on=datetime.fromtimestamp(_dict.get("updated_on")),
                   classified_field_filters=_dict.get("classified_field_filters"),
                   category=_dict.get("category"),
                   search_fields=SearchFieldsMapper.dict_to_model(_dict=_dict.get("search_fields")),
                   tag=_dict.get("tag"),
                   data=DataMapper.dict_to_model(_dict=_dict.get("data")),
                   pull_requests=set())
