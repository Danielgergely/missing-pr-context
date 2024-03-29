from models.pr import User, Approval
from datetime import datetime


class UserMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> User:
        return User(email=_dict.get("email"),
                    name=_dict.get("name"),
                    username=_dict.get("username"))


class ApprovalMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Approval:
        return Approval(by=UserMapper.dict_to_model(_dict.get("by")),
                        description=_dict.get("description"),
                        grantedOn=datetime.fromtimestamp(_dict.get("grantedOn")),
                        type=_dict.get("type"),
                        value=_dict.get("value"))
