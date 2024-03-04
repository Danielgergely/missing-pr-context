from mapper.bug import IssueTypeMapper, ProjectMapper, VersionMapper, WatchesMapper, PriorityMapper, UserMapper, \
    StatusMapper, ComponentMapper, VotesMapper
from models.bug import Fields

from datetime import datetime


class FieldsMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Fields:
        return Fields(issuetype=IssueTypeMapper.dict_to_model(_dict=_dict.get("issuetype")),
                      timespent=_dict.get("timespent"),
                      project=ProjectMapper.dict_to_model(_dict=_dict.get("project")),
                      fixVersions=[VersionMapper.dict_to_model(_dict=version) for version in _dict.get("fixVersions")],
                      aggregatetimespent=_dict.get("aggregatetimespent"),
                      resolution=_dict.get("resolution"),
                      resolutiondate=datetime.fromtimestamp(_dict.get("resolutiondate")) if _dict.get(
                          "resolutiondate") is not None else None,
                      workratio=_dict.get("workratio"),
                      lastViewed=_dict.get("lastViewed"),
                      watches=WatchesMapper.dict_to_model(_dict=_dict.get("watches")),
                      created=datetime.strptime(_dict.get("created"), "%Y-%m-%dT%H:%M:%S.%f%z"),
                      priority=PriorityMapper.dict_to_model(_dict=_dict.get("priority")),
                      labels=_dict.get("labels"),
                      timeestimate=_dict.get("timeestimate"),
                      aggregatetimeoriginalestimate=_dict.get("aggregatetimeoriginalestimate"),
                      versions=[VersionMapper.dict_to_model(_dict=version) for version in _dict.get("versions")],
                      issuelinks=_dict.get("issueLinks"),
                      assignee=UserMapper.dict_to_model(_dict=_dict.get("assignee")),
                      updated=datetime.strptime(_dict.get("updated"), "%Y-%m-%dT%H:%M:%S.%f%z"),
                      status=StatusMapper.dict_to_model(_dict=_dict.get("status")),
                      components=[ComponentMapper.dict_to_model(_dict=component) for component in
                                  _dict.get("components")],
                      timeoriginalestimate=_dict.get("timeoriginalestimate"),
                      description=_dict.get("description"),
                      aggregatetimeestimate=_dict.get("aggregatetimeestimate"),
                      summary=_dict.get("summary"),
                      creator=UserMapper.dict_to_model(_dict=_dict.get("creator")),
                      subtasks=[subtask for subtask in _dict.get("subtasks")],
                      reporter=UserMapper.dict_to_model(_dict=_dict.get("reporter")),
                      aggregateprogress=_dict.get("aggregateprogress"),
                      environment=_dict.get("environment"),
                      progress=_dict.get("progress"),
                      votes=VotesMapper.dict_to_model(_dict=_dict.get("votes")),
                      customfields=[_dict[key] for key in _dict.keys() if 'customfield_' in key[:12]])
