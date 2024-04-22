import re
from datetime import datetime

from mapper.bug import UserMapper
from mapper.pr import PatchSetMapper
from models.pr import PullRequestLight, PRStatus


class PullRequestLightMapper:

    @staticmethod
    def dict_to_model(_dict: dict, bugs: dict, bots: [str]) -> PullRequestLight:
        data = _dict.get("data")
        created_on = datetime.fromtimestamp(data.get("createdOn"))
        commit_message = data.get("commitMessage")
        patchSets = [PatchSetMapper.dict_to_model(patch_set) for patch_set in data.get("patchSets", [])]
        human_approvals = [approval for patchSet in patchSets for approval in patchSet.approvals
                           if approval.by.name not in bots and approval.value == "2"]
        if human_approvals:
            latest_approval = max(human_approvals, key=lambda a: a.grantedOn, default=None)
            approved_by = latest_approval.by
            approved_time = latest_approval.grantedOn
            time_difference = approved_time - created_on
            processing_time = int(time_difference.total_seconds() / 3600)
        else:
            approved_by = None
            approved_time = None
            processing_time = None
        commit_word_count = len(commit_message.split())
        bug_search_pattern = r"Task-number: "
        commit_search = commit_message.replace("\n", " ")
        match = re.search(bug_search_pattern, commit_search)
        if match:
            bug_linked = True
            pr_bug_id = commit_search[match.end():match.end() + 11]
            bug = bugs.get(pr_bug_id)
            if bug is not None:
                bug.pull_requests.add(data.get("number"))
                bug_description = bug.data.fields.description
                try:
                    bug_description_word_count = len(bug.data.fields.description.split())
                except Exception as e:
                    print(pr_bug_id)
                    print(e)
                    bug_description_word_count = 0
                bug_reopened = False
            else:
                bug_description = None
                bug_description_word_count = 0
                bug_reopened = False
        else:
            bug_linked = False
            pr_bug_id = None
            bug_description = None
            bug_description_word_count = None
            bug_reopened = None
        return PullRequestLight(category=_dict.get("category"),
                                timestamp=datetime.fromtimestamp(_dict.get("timestamp")),
                                updated_on=datetime.fromtimestamp(_dict.get("updated_on")),
                                created_on=created_on,
                                commitMessage=commit_message,
                                lastUpdated=datetime.fromtimestamp(data.get("lastUpdated")),
                                number=data.get("number"),
                                open=data.get("open"),
                                owner=UserMapper.dict_to_model(data.get("owner")),
                                project=data.get("project"),
                                status=PRStatus(data.get("status")),
                                subject=data.get("subject"),
                                processingTime=processing_time,
                                approvedBy=approved_by,
                                approvedTime=approved_time,
                                commitWordCount=commit_word_count,
                                bugLinked=bug_linked,
                                bugId=pr_bug_id,
                                bugDescription=bug_description,
                                bugDescriptionWordCount=bug_description_word_count,
                                iterationCount=len(patchSets),
                                bugReopened=bug_reopened)
