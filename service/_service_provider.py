import pandas as pd

from evaluator import Evaluator
from file_reader import FileReader
from config import Config, app_config
from models.pr import PullRequestLight
from statistics import PRStatistics
from visualizer import Visualizer


class ServiceProvider:
    _config: Config

    def __init__(self, config: Config):
        self._config = config

    def file_reader(self, data_directory: str = "data") -> FileReader:
        return FileReader(data_directory=data_directory)

    def pr_statistics(self, pull_requests: [PullRequestLight]) -> PRStatistics:
        return PRStatistics(pull_requests=pull_requests)

    def visualizer(self, data: pd.DataFrame) -> Visualizer:
        return Visualizer(data=data)

    def evaluator(self, data: pd.DataFrame, columns_to_compare: [tuple]) -> Evaluator:
        return Evaluator(data=data, columns_to_compare=columns_to_compare)


service_provider = ServiceProvider(config=app_config)
