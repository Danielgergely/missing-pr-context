from models import Data
from mapper import MessageMapper, PatchSetMapper
from models import User


class UserMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> User:
        return User(email=_dict.get("email"),
                    name=_dict.get("name"),
                    username=_dict.get("username"))


class DataMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Data:
        return Data(branch=_dict.get("branch"),
                    comments=[MessageMapper.dict_to_model(message) for message in _dict.get("comments")],
                    commitMessage=_dict.get("commitMessage"),
                    createdOn=_dict.get("createdOn"),
                    id=_dict.get("id"),
                    lastUpdated=_dict.get("lastUpdated"),
                    number=_dict.get("number"),
                    open=_dict.get("open"),
                    owner=UserMapper.dict_to_model(_dict=_dict.get("owner")),
                    patchSets=[PatchSetMapper.dict_to_model(patch_set) for patch_set in _dict.get("patchSets", [])],
                    project=_dict.get("project"),
                    status=_dict.get("status"),
                    subject=_dict.get("subject"),
                    url=_dict.get("url"))
