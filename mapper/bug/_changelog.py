from mapper.bug import HistoryMapper
from models.bug import Changelog


class ChangelogMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Changelog:
        return Changelog(startAt=_dict.get("startAt"),
                         maxResults=_dict.get("maxResults"),
                         total=_dict.get("total"),
                         histories=[HistoryMapper.dict_to_model(_dict=history) for history in _dict.get("histories")])
