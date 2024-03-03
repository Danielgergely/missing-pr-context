import json
import os
from io import StringIO

import pandas as pd


class FileReader:
    _data_directory: str

    def __init__(self, data_directory: str = "data"):
        self._data_directory = data_directory

    def read_json(self, file_path: str):
        file_path = os.path.join(os.getcwd(), self._data_directory, file_path)
        with open(file=file_path, mode='r') as file:
            lines = file.readlines()
        return [json.loads(line) for line in lines]

    def read_txt(self, file_path: str):
        file_path = os.path.join(os.getcwd(), self._data_directory, file_path)
        with open(file=file_path, mode="r") as file:
            return file.read()

    def json_to_df(self, file_path: str):
        lines = (self.read_json(file_path=file_path))
        json_content = '[' + ','.join(lines) + ']'
        return pd.read_json(StringIO(json_content))
