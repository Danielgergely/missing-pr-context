from file_reader import FileReader
from config import Config, app_config


class ServiceProvider:
    _config: Config

    def __init__(self, config: Config):
        self._config = config

    def file_reader(self, data_directory: str = "data") -> FileReader:
        return FileReader(data_directory=data_directory)


service_provider = ServiceProvider(config=app_config)
