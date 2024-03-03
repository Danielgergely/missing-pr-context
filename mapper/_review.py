from models import Review
from mapper import DataMapper, SearchFieldsMapper


class ReviewMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Review:
        return Review(backend_name=_dict.get("backend_name"),
                      backend_version=_dict.get("backend_version"),
                      category=_dict.get("category"),
                      classified_fields_filtered=_dict.get("classified_fields_filtered"),
                      data=DataMapper.dict_to_model(_dict=_dict.get("data")),
                      origin=_dict.get("origin"),
                      perceval_version=_dict.get("perceval_version"),
                      search_fields=SearchFieldsMapper.dict_to_model(_dict=_dict.get("search_fields")),
                      tag=_dict.get("tag"),
                      timestamp=_dict.get("timestamp"),
                      updated_on=_dict.get("updated_on"),
                      uuid=_dict.get("uuid"))
