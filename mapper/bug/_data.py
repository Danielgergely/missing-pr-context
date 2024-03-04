from mapper.bug import FieldsMapper, ChangelogMapper
from models.bug import Data


class DataMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Data:
        return Data(expand=_dict.get("expand"),
                    id=_dict.get("id"),
                    self=_dict.get("self"),
                    fields=FieldsMapper.dict_to_model(_dict=_dict.get("fields")),
                    renderedFields=_dict.get("renderedFields"),
                    transitions=_dict.get("transitions"),
                    operations=_dict.get("operations"),
                    changelog=ChangelogMapper.dict_to_model(_dict=_dict.get("changelog")),
                    comments_data=_dict.get("comments_data", []))
