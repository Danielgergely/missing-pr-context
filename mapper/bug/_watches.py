from models.bug import Watches


class WatchesMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Watches:
        return Watches(self=_dict.get("self"),
                       watchCount=_dict.get("watchCount"),
                       isWatching=_dict.get("isWatching"))
