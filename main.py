from mapper.bug import BugMapper
from mapper.pr import PullRequestLightMapper
from models.bug import Bug
from service import service_provider


def read_qt_bots(qt_bots_file_path: str):
    f_reader = service_provider.file_reader()
    return [f_reader.read_txt(qt_bots_file_path).split("\n")]


def read_bug_data(bug_data_file_path: str, bug_data_pickle_path: str, full_load: bool = True):
    f_reader = service_provider.file_reader()
    if f_reader.file_exists(bug_data_pickle_path) and not full_load:
        return f_reader.pickle_to_data(bug_data_pickle_path)
    else:
        bug_data = f_reader.read_json(bug_data_file_path)
        bugs = [BugMapper.dict_to_model(bug) for bug in bug_data]
        f_reader.data_to_pickle(bug_data_pickle_path, bugs)
        return bugs


def read_pr_data(pr_data_file_path: str, pr_data_pickle_path: str, bugs: [Bug], bugIds: [str], qt_bots: [str],
                 full_load: bool = True):
    f_reader = service_provider.file_reader()
    if f_reader.file_exists(pr_data_pickle_path) and not full_load:
        return f_reader.pickle_to_data(pr_data_pickle_path)
    else:
        pr_data = f_reader.read_json(pr_data_file_path)
        pull_requests = [PullRequestLightMapper.dict_to_model(pr, bugIds=bugIds, bugs=bugs, bots=qt_bots) for pr in
                         pr_data]
        f_reader.data_to_pickle(pr_data_pickle_path, pull_requests)
        return pull_requests


if __name__ == '__main__':
    bug_full_load = False
    pr_full_load = False

    qt_bots = read_qt_bots(qt_bots_file_path="qt_bots.txt")

    bugs = read_bug_data(bug_data_file_path="0_jira_Qt_2021-09-21.json",
                         bug_data_pickle_path="qt_bugs.pickle",
                         full_load=bug_full_load)
    bugIds = [bug.search_fields.issue_key for bug in bugs]

    pull_requests = read_pr_data(pr_data_file_path="qt_2017-01-01.json",
                                 pr_data_pickle_path="pr_data.pickle",
                                 bugs=bugs,
                                 bugIds=bugIds,
                                 qt_bots=qt_bots,
                                 full_load=pr_full_load)

    if pr_full_load:  # save bugs again if prs are loaded -> pr numbers added to bugs
        f_reader = service_provider.file_reader()
        f_reader.data_to_pickle("qt_bugs.pickle", bugs)

    a = 10

    # QT
    # PR 5 -> QTBUG-85700 (Task number:) -> https://codereview.qt-project.org/c/qt/qtbase/+/285578
    # PR 7 -> QTBUG-86969 (Task number:) -> https://codereview.qt-project.org/c/qt/qtbase/+/315655
    # PR 18 -> QTBUG-86133 (Task number:) -> https://codereview.qt-project.org/c/qt/qtbase/+/314853

    # Eclipse
    # -> bug data is not exported completely. the data column only contains a small portion of the actual information

    # Bug reopen -> transitions ❌
        ## bug data does not contain transition data. Transitions is always an empty list -> 'QTBUG-23917'
    # multiple PR for 1 bug ✅
    # iteration count-> patch sets number of commits after review ✅
        ## https://codereview.qt-project.org/c/qt/qtbase/+/311411 -> 104 iterationCount = 4
    # List all PR statuses ✅
