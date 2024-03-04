from models.bug import Status


class StatusMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Status:
        return Status(self=_dict.get("self"),
                      description=_dict.get("description"),
                      iconUrl=_dict.get("iconUrl"),
                      name=_dict.get("name"),
                      id=_dict.get("id"),
                      statusCategory=_dict.get("statusCategory"))
