from mapper.bug import BugMapper
from mapper.pr import PullRequestLightMapper
import pandas as pd
from models.pr import PullRequestLight
from service import service_provider
from statistics import PRStatistics
from visualizer import Visualizer


def read_qt_bots(qt_bots_file_path: str):
    f_reader = service_provider.file_reader()
    return f_reader.read_txt(qt_bots_file_path).split("\n")


def read_bug_data(bug_data_file_path: str, bug_data_pickle_path: str, full_load: bool = True):
    f_reader = service_provider.file_reader()
    if f_reader.file_exists(bug_data_pickle_path) and not full_load:
        return f_reader.pickle_to_data(bug_data_pickle_path)
    else:
        bug_data = f_reader.read_json(bug_data_file_path)
        bugs = [BugMapper.dict_to_model(bug) for bug in bug_data]
        bug_dict = {bug.search_fields.issue_key: bug for bug in bugs}
        f_reader.data_to_pickle(bug_data_pickle_path, bug_dict)
        return bug_dict


def read_pr_data(pr_data_file_path: str, pr_data_pickle_path: str, bugs: dict, qt_bots: [str],
                 full_load: bool = True):
    f_reader = service_provider.file_reader()
    if f_reader.file_exists(pr_data_pickle_path) and not full_load:
        return f_reader.pickle_to_data(pr_data_pickle_path)
    else:
        pr_data = f_reader.read_json(pr_data_file_path)
        pull_requests = [PullRequestLightMapper.dict_to_model(pr, bugs=bugs, bots=qt_bots) for pr in
                         pr_data]
        f_reader.data_to_pickle(pr_data_pickle_path, pull_requests)
        return pull_requests


def calculate_statistics(pull_requests: [PullRequestLight]):
    pr_statistics = PRStatistics(pull_requests=pull_requests)
    print(f"% of Pull Request with linked bugs: {pr_statistics.percentage_of_prs_with_bugs():.2f}%")
    statistics = pr_statistics.calculate_statistics()
    return pd.DataFrame(statistics)


def visualize(data: pd.DataFrame, x_values: list,
              title: str = "Pull Request statistics", barplot: bool = True):
    visualizer = Visualizer(data=data)
    main_categories = ["Missing linkage", "Insufficient context", "Proper context"]
    sub_category = [("Comment count", "box"),
                    ("Review time", "box"),
                    ("Review iteration", "box"),
                    ("Abandoned PR", "bar")]
    visualizer.create_combined_plot(main_categories=main_categories,
                                    sub_categories=sub_category,
                                    title=title)
    if barplot:
        visualizer.create_barplots(
            x_values=x_values,
            title=title)
    else:
        visualizer.create_boxplots(
            x_values=x_values,
            title=title)


if __name__ == '__main__':
    bug_full_load = False
    pr_full_load = False

    qt_bots = read_qt_bots(qt_bots_file_path="qt_bots.txt")

    bugs = read_bug_data(bug_data_file_path="0_jira_Qt_2021-09-21.json",
                         bug_data_pickle_path="qt_bugs.pickle",
                         full_load=bug_full_load)

    pull_requests = read_pr_data(pr_data_file_path="qt_2017-01-01.json",
                                 pr_data_pickle_path="pr_data.pickle",
                                 bugs=bugs,
                                 qt_bots=qt_bots,
                                 full_load=pr_full_load)

    if pr_full_load:  # save bugs again if prs are loaded -> pr numbers added to bugs
        f_reader = service_provider.file_reader()
        f_reader.data_to_pickle("qt_bugs.pickle", bugs)

    statistics = calculate_statistics(pull_requests=pull_requests)

    visualize(data=statistics, x_values=[("Review time", "PR category"),
                                         ("Review iteration", "PR category"),
                                         ("Abandoned PR", "PR category"),
                                         ("Comment count", "PR category")],
              barplot=False)

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
    ## user revision hash -> unique number of hashes
    # List all PR statuses ✅
    # useful statistics -> % of pr to bugs ✅ -> iteration < 3 > 3 ✅ -> time + 2 day -2 days ✅

    ## 2024.04.08
    # Eclipse data -> csv ❔
    # Bug reopen -> transitions ❔

    # number of words + 30 -> dynamic ✅
    # review comments count ✅
    # bug id duplicated -> reopened ❔
    # normalize data before visualization ❔-> is it necessary if concept is ok
    # come up with meaningful visualizations -> boxplots -> concept created ✅

    ## 2024.04.22
    # Abandoned/not abandoned -> use barchart
    # Implement new version according to concept
    # Add y & x-axis titles ✅
    # Statistical methods
    # Start preparing presentation -> !!answer all questions in email!!
