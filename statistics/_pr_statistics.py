from models.bug import Bug
from models.pr import PullRequestLight


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
    def resolving_time(pr: PullRequestLight) -> str:
        if pr.processingTime < (24 * 3):
            return '< 3 days'
        else:
            return '>= 3 days'

    @staticmethod
    def iteration_count(pr: PullRequestLight) -> str:
        if pr.iterationCount < 3:
            return '< 3'
        else:
            return '>= 3'
