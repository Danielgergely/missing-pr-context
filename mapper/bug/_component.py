from models.bug import Component


class ComponentMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Component:
        return Component(self=_dict.get("self"),
                         id=_dict.get("id"),
                         name=_dict.get("name"))
