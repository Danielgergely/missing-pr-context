from models.bug import Item


class ItemMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Item:
        return Item(field=_dict.get("field"),
                    fieldType=_dict.get("fieldType"),
                    from_=_dict.get("from"),
                    fromString=_dict.get("fromString"),
                    to=_dict.get("to"),
                    toString=_dict.get("toString"))
