from mapper.bug import BugMapper
from mapper.pr import PullRequestMapper, PullRequestLightMapper
from service import service_provider

if __name__ == '__main__':
    f_reader = service_provider.file_reader()

    new_load = True

    if f_reader.file_exists("pr_data.pickle") and not new_load:
        pull_requests = f_reader.pickle_to_data("pr_data.pickle")
        a = 10
    else:
        service_provider = service_provider
        qt_bots = [f_reader.read_txt("qt_bots.txt").split("\n")]

        # bug_data = f_reader.read_json("bug_test_qt.json")
        bug_data = f_reader.read_json("0_jira_Qt_2021-09-21.json")
        # bug_data = f_reader.csv_to_json("eclipse_reopened_2022-03-04.csv")
        bugs = [BugMapper.dict_to_model(bug) for bug in bug_data]
        bugIds = [bug.search_fields.issue_key for bug in bugs]
        # pr_data = f_reader.read_json("test2.json")
        pr_data = f_reader.read_json("qt_2017-01-01.json")
        # pr_data = f_reader.read_json("eclipse.json")
        pull_requests = [PullRequestLightMapper.dict_to_model(pr, bugIds=bugIds, bugs=bugs, bots=qt_bots) for pr in pr_data[:50]]
        # pull_requests = [PullRequestMapper.dict_to_model(pr) for pr in pr_data[:50]]
        f_reader.data_to_pickle("pr_data.pickle", pull_requests)

        a = 10

    # QT
    # PR 5 -> QTBUG-85700 (Task number:) -> https://codereview.qt-project.org/c/qt/qtbase/+/285578
    # PR 7 -> QTBUG-86969 (Task number:) -> https://codereview.qt-project.org/c/qt/qtbase/+/315655
    # PR 18 -> QTBUG-86133 (Task number:) -> https://codereview.qt-project.org/c/qt/qtbase/+/314853

    # Eclipse
    # -> bug data is not exported completely. the data column only contains a small portion of the actual information


    # Bug reopen -> transitions
    # multiple PR for 1 bug
    # iteration count-> patch sets number of commits after review
    # List all PR statuses ✅
