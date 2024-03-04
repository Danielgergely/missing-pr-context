from mapper.bug import ProjectCategoryMapper
from models.bug import Project


class ProjectMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Project:
        return Project(self=_dict.get("self"),
                       id=_dict.get("id"),
                       key=_dict.get("key"),
                       name=_dict.get("name"),
                       projectTypeKey=_dict.get("projectTypeKey"),
                       avatarUrls=_dict.get("avatarUrls"),
                       projectCategory=ProjectCategoryMapper.dict_to_model(_dict=_dict.get("projectCategory")))
