from models.bug import ProjectCategory


class ProjectCategoryMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> ProjectCategory:
        return ProjectCategory(self=_dict.get("self"),
                               id=_dict.get("id"),
                               description=_dict.get("description"),
                               name=_dict.get("name"))
