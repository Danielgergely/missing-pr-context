from models.pr import Comment, User


class UserMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> User:
        return User(email=_dict.get("email"),
                    name=_dict.get("name"),
                    username=_dict.get("username"))


class CommentMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Comment:
        return Comment(file=_dict.get("file"),
                       line=_dict.get("line"),
                       message=_dict.get("message"),
                       reviewer=UserMapper.dict_to_model(_dict=_dict.get("reviewer")))
