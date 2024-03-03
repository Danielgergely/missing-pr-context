from models import Approval
from mapper import UserMapper


class ApprovalMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Approval:
        return Approval(by=UserMapper.dict_to_model(_dict.get("by")),
                        description=_dict.get("description"),
                        grantedOn=_dict.get("grantedOn"),
                        type=_dict.get("type"),
                        value=_dict.get("value"))
