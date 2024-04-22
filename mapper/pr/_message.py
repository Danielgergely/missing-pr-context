from models.pr import Message, User
from datetime import datetime


class UserMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> User | None:
        if _dict is not None:
            return User(email=_dict.get("email"),
                        name=_dict.get("name"),
                        username=_dict.get("username"))
        else:
            return None


class MessageMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Message:
        return Message(message=_dict.get("message"),
                       reviewer=UserMapper.dict_to_model(_dict=_dict.get("reviewer")),
                       timestamp=datetime.fromtimestamp(_dict.get("timestamp")))
