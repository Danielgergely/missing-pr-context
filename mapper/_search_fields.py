from models import SearchFields


class SearchFieldsMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> SearchFields:
        return SearchFields(item_id=_dict.get("item_id"),
                            project_name=_dict.get("project_name"),
                            review_hash=_dict.get("review_hash"))
