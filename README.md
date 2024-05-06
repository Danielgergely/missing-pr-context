# Missing PR Context Analysis

This project is a Python application that analyzes the context of Pull Requests (PRs). It categorizes PRs into three categories:
- Missing linkage (no issues linked to the PR)
- Short Description (description in PR and linked issue is less than the defined threshold)
- Sufficient context (an issue is linked and there is enough description in both the PR and the issue)


## Features

- Reads PR data and bug data from JSON/text files.
- Converts the raw data into python classes.
- Calculates various statistics related to PRs.
- Visualizes the calculated statistics using Plotly.

## How to Run

1. Ensure that you have Python and pip installed on your system.
2. Clone this repository.
3. Extract the data from the `data.zip` file. (Add your data to this folder if you want to analyze a different project).
4. Install the required dependencies.
5. Run the `main.py` script.

## Code Overview

The main components of this project are:

- [`FileReader`](./file_reader/_file_reader.py): This class is responsible for reading data from various file formats, converting them to `pd.DataFrame`, and pickling objects for faster processing.
- [`Bug`](./models/bug/_bug.py), [`PullRequest`](./models/pr/_pull_request.py) and [`PullRequestLight`](./models/pr/_pr_light.py): These classes represent bug and PR data, respectively. Instead of using a complex nested dictionary, these classes can be used to interpret data in a more structured way.
- [`BugMapper`](./mapper/bug/_bug.py) and [`PullRequestMapper`](./mapper/pr/_pull_request.py): These classes are responsible for mapping raw data to the corresponding classes. [`PullRequestLightMapper`](./mapper/pr/_pr_light.py) is a lightweight version of the `PullRequestMapper` class, where irrelevant PR & Bug data is ignored, bugs are linked to PRs and relevant features are extracted. 
- [`ServiceProvider`](./service/_service_provider.py): This class is responsible for the providing of the available services to the project. Currently supported services are reading data, calculating statistics, and visualizing data.
- [`Statistics`](./statistics/_pr_statistics.py): This class is responsible for calculating various statistics related to PRs.
- [`Visualizer`](./visualizer/_visualizer.py): This class is responsible for visualizing the calculated statistics using Plotly.

## Reproducibility
- The raw data is stored in the `data` directory. The pull request data was exported using Gerrit's REST API, and the bug data comes from [here](https://bugreports.qt.io).
- As the eclipse data is only a partial data with missing fields, the whole analysis was only done for the QT project.
- Exported data is from 2017.
- To reproduce the analysis for a different project, do the following steps:
  - Make sure your data is in the required format (look at [`qt_2017-01-01.json`](./data/qt_2017-01-01.json) and [`0_qt_jira_QT_2021-09-21.json`](./data/0_jira_Qt_2021-09-21.json) for reference).
  - Change the file paths in the `main.py` script.
  - If you have bots, which you want to ignore during the analysis, create a .txt file and use [`qt_bots.txt`](./data/qt_bots.txt) as a reference.
  - If loading for the first time, change `bug_full_load` and `pr_full_load` to `True` in the `main.py` script. (This will take some time to load the data).
  - If you want different statistics, you can change them in the [`_pr_statistics.py`](./statistics/_pr_statistics.py) file.
  - Define what categories should be visualized in the `main.py` script. If using the combined charts, you can choose between a light or a dark theme.
  - Run the `main.py` script.

## Future Work
- Improve the visualization of data.
- Add more statistical methods for analyzing PRs.
- Handle outliers in the data.
- Automatic export of data.


***Note:*** *This project is the result of the Empirical Software Engineering Seminar at the University of Zurich, Spring 2024. Supervisor: Shirin Pirouzkhah*