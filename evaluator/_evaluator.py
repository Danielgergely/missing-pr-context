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
        for column_pair in self._columns_to_compare:
            x = pd.Series(self._data[column_pair[0]])
            y = pd.Series(self._data[column_pair[1]])
            result = scipy.stats.mannwhitneyu(x, y)
            print(f"Column pair: {column_pair}. Mann-Whitney U test result: {result.statistic}")

    def chi_squared_test(self):
        for column_pair in self._columns_to_compare:
            x = pd.Series(self._data[column_pair[0]])
            y = pd.Series(self._data[column_pair[1]])
            contingency_table = pd.crosstab(x, y)
            result = scipy.stats.chi2_contingency(contingency_table)
            print(f"Column pair: {column_pair}. Chi-Square test result: result: {result.statistic}")
