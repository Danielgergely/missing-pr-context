import pandas as pd

from models.pr import PullRequestLight
import scipy


class Evaluator:
    _data: [PullRequestLight]
    _columns_to_compare: [tuple]
    _stats_df: pd.DataFrame

    def __init__(self, data: [PullRequestLight], columns_to_compare: [tuple]):
        self._data = data
        self._columns_to_compare = columns_to_compare
        self._stats_df = pd.DataFrame([pr.to_dict() for pr in data])

    def mann_whitney_u_test(self):
        for column_pair in self._columns_to_compare:
            x = pd.Series(self._stats_df[column_pair[0]])
            y = pd.Series(self._stats_df[column_pair[1]])
            result = scipy.stats.mannwhitneyu(x, y)
            print(f"Column pair: {column_pair}. Mann-Whitney U test result: {result}")
