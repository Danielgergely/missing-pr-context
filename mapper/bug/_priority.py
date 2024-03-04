from models.bug import Priority


class PriorityMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Priority:
        return Priority(self=_dict.get("self"),
                        iconUrl=_dict.get("iconUrl"),
                        name=_dict.get("name"),
                        id=_dict.get("id"))
