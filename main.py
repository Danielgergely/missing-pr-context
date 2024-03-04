from mapper.bug import BugMapper
from mapper.pr import PullRequestMapper
from service import service_provider

if __name__ == '__main__':
    service_provider = service_provider
    f_reader = service_provider.file_reader()
    qt_bots = [f_reader.read_txt("qt_bots.txt").split("\n")]

    bug_data = f_reader.read_json("bug_test_qt.json")
    bugs = [BugMapper.dict_to_model(bug) for bug in bug_data[:50]]
    # pr_data = f_reader.read_json("test2.json")
    pr_data = f_reader.read_json("qt_2017-01-01.json")
    # pr_data = f_reader.read_json("eclipse.json")
    pull_requests = [PullRequestMapper.dict_to_model(pr) for pr in pr_data[:50]]

    a = 10
