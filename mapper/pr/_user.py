from models.pr import User


class UserMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> User:
        return User(email=_dict.get("email"),
                    name=_dict.get("name"),
                    username=_dict.get("username"))
