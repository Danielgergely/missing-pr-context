from models import Message
from mapper import UserMapper


class MessageMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Message:
        return Message(message=_dict.get("message"),
                       reviewer=UserMapper.dict_to_model(dict=_dict.get("reviewer")),
                       timestamp=_dict.get("timestamp"))
