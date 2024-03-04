from models.bug import User


class UserMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> User:
        return User(self=_dict.get("self"),
                    name=_dict.get("name"),
                    key=_dict.get("key"),
                    avatarUrls=_dict.get("avatarUrls"),
                    displayName=_dict.get("displayName"),
                    active=_dict.get("active"),
                    timeZone=_dict.get("timeZone"))
