from models import Message
from models import User


class UserMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> User:
        return User(email=_dict.get("email"),
                    name=_dict.get("name"),
                    username=_dict.get("username"))


class MessageMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Message:
        return Message(message=_dict.get("message"),
                       reviewer=UserMapper.dict_to_model(_dict=_dict.get("reviewer")),
                       timestamp=_dict.get("timestamp"))
