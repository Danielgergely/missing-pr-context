from models.bug import Version


class VersionMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Version:
        return Version(self=_dict.get("self"),
                       id=_dict.get("id"),
                       description=_dict.get("description"),
                       name=_dict.get("name"),
                       archived=_dict.get("archived"),
                       release=_dict.get("release"))
