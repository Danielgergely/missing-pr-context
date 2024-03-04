from mapper.bug import UserMapper, ItemMapper
from models.bug import History
from datetime import datetime


class HistoryMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> History:
        return History(author=UserMapper.dict_to_model(_dict.get("author")),
                       created=datetime.strptime(_dict.get("created"), "%Y-%m-%dT%H:%M:%S.%f%z"),
                       items=[ItemMapper.dict_to_model(_dict=item) for item in _dict.get("items")])
