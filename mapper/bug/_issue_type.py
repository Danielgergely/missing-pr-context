from models.bug import IssueType


class IssueTypeMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> IssueType:
        return IssueType(self=_dict.get("self"),
                         id=_dict.get("id"),
                         description=_dict.get("description"),
                         iconUrl=_dict.get("iconUrl"),
                         name=_dict.get("name"),
                         subtask=_dict.get("subtask"),
                         avatarId=_dict.get("avatarId"))
