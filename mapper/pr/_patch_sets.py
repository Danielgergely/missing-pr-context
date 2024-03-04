from models import PatchSet
from mapper.pr._approval import ApprovalMapper
from models import User
from datetime import datetime


class UserMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> User:
        return User(email=_dict.get("email"),
                    name=_dict.get("name"),
                    username=_dict.get("username"))


class PatchSetMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> PatchSet:
        return PatchSet(approvals=[ApprovalMapper.dict_to_model(approval) for approval in _dict.get("approvals", [])],
                        author=UserMapper.dict_to_model(_dict=_dict.get("author")),
                        createdOn=datetime.fromtimestamp(_dict.get("createdOn")),
                        kind=_dict.get("kind"),
                        number=_dict.get("number"),
                        parents=[parent for parent in _dict.get("parents")],
                        ref=_dict.get("ref"),
                        revision=_dict.get("revision"),
                        sizeDeletions=_dict.get("sizeDeletions"),
                        sizeInsertions=_dict.get("sizeInsertions"),
                        uploader=UserMapper.dict_to_model(_dict.get("uploader")))
