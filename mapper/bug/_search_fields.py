from models.bug import SearchFields


class SearchFieldsMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> SearchFields:
        return SearchFields(issue_key=_dict.get("issue_key"),
                            item_id=_dict.get("item_id"),
                            project_id=_dict.get("project_id"),
                            project_key=_dict.get("project_key"),
                            project_name=_dict.get("project_name"))
