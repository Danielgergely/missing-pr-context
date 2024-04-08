from models.bug import Bug
from models.pr import PullRequestLight, PRStatus


class PRStatistics:
    _bugs: [Bug]
    _pull_requests: [PullRequestLight]
    _bugIds: [str]

    def __init__(self, pull_requests: [PullRequestLight], bugs: [Bug], bug_ids: [str]):
        self._pull_requests = pull_requests
        self._bugs = bugs
        self._bugIds = bug_ids

    #### Data set statistics ###

    def percentage_of_prs_with_bugs(self) -> float:
        prs_with_bugs = sum(1 for pr in self._pull_requests if pr.bugLinked)
        return prs_with_bugs / len(self._pull_requests) * 100

    ### PR statistics ###

    @staticmethod
    def review_time(pr: PullRequestLight) -> str:
        if pr.processingTime < (24 * 3):
            return '< 3 days'
        else:
            return '>= 3 days'

    @staticmethod
    def review_iteration(pr: PullRequestLight) -> str:
        if pr.iterationCount < 3:
            return '< 3'
        else:
            return '>= 3'

    @staticmethod
    def pr_category(pr: PullRequestLight, required_line_count: int = 2,
                    required_bug_description_line_count: int = 2) -> str:
        match (pr.bugLinked, pr.commitLineCount >= required_line_count,
               pr.bugDescriptionLineCount >= required_bug_description_line_count):
            case (False, False, _):  # 🔗❌ | 💬❌ | 🐞❌
                return 'Insufficient context'
            case (False, True, _):  # 🔗❌ | 💬✅ | 🐞❌
                return 'Missing linkage'
            case (True, False, _):  # 🔗✅ | 💬❌ | 🐞❌
                return 'Insufficient context'
            case (True, True, False):  # 🔗✅ | 💬✅ | 🐞❌
                return 'Insufficient bug description'
            case (True, True, True):  # 🔗✅ | 💬✅ | 🐞✅
                return 'Proper context'

    @staticmethod
    def abandoned_pr(pr: PullRequestLight) -> str:
        if pr.status == PRStatus.ABANDONED:
            return 'Abandoned'
        else:
            return 'Not abandoned'

