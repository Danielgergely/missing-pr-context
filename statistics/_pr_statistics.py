from models.pr import PullRequestLight, PRStatus


class PRStatistics:
    _pull_requests: [PullRequestLight]

    def __init__(self, pull_requests: [PullRequestLight]):
        self._pull_requests = pull_requests

    #### Data set statistics ###

    def percentage_of_prs_with_bugs(self) -> float:
        prs_with_bugs = sum(1 for pr in self._pull_requests if pr.bugLinked)
        return prs_with_bugs / len(self._pull_requests) * 100

    ### PR statistics ###

    @staticmethod
    def comment_count(pr: PullRequestLight) -> str:
        count = pr.commentCount
        match count:
            case 0:
                return "0"
            case _ if 1 <= count < 6:
                return "1 - 5"
            case _ if 6 <= count < 11:
                return "6 - 10"
            case _ if 11 <= count < 26:
                return "11 - 25"
            case _ if 26 <= count < 101:
                return "26 - 100"
            case _:
                return "100+"

    @staticmethod
    def review_time(pr: PullRequestLight) -> str:
        if pr.processingTime is None:
            return 'N/A'
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
    def pr_category(pr: PullRequestLight, required_word_count: int = 30,
                    required_bug_description_word_count: int = 30) -> str:
        bug_description_word_count = pr.bugDescriptionWordCount or 0
        match (pr.bugLinked, pr.commitWordCount >= required_word_count,
               bug_description_word_count >= required_bug_description_word_count):
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

    def calculate_statistics(self, **kwargs):
        return [
            {
                'PR': pr.number,
                'Review time': self.review_time(pr),
                'Review iteration': self.review_iteration(pr),
                'PR category': self.pr_category(pr, **kwargs),
                'Abandoned PR': self.abandoned_pr(pr),
                'Comment count': self.comment_count(pr),
            }
            for pr in self._pull_requests
        ]
