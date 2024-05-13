import pandas as pd

from models.pr import PullRequestLight
import scipy


class Evaluator:
    _data: pd.DataFrame
    _columns_to_compare: [tuple]

    def __init__(self, data: pd.DataFrame, columns_to_compare: [tuple]):
        self._data = data
        self._columns_to_compare = columns_to_compare

    def mann_whitney_u_test(self):
        result_dict = {}
        for column_pair in self._columns_to_compare:
            x = pd.Series(self._data[column_pair[0]])
            y = pd.Series(self._data[column_pair[1]])
            result = scipy.stats.mannwhitneyu(x, y)
            print(f"Column pair: {column_pair}. Mann-Whitney U test result: {result.statistic}")
            result_dict[column_pair] = result.statistic
        return result_dict

    def chi_squared_test(self):
        result_dict = {}
        for column_pair in self._columns_to_compare:
            x = pd.Series(self._data[column_pair[0]])
            y = pd.Series(self._data[column_pair[1]])
            x = (x + 0.0001) / (x + 0.0001).sum()
            y = (y + 0.0001) / (y + 0.0001).sum()
            result = scipy.stats.chisquare(x, y)
            print(f"Column pair: {column_pair}. Chi-Square test result: result: {result.statistic}")
            result_dict[column_pair] = result.statistic
        return result_dict
