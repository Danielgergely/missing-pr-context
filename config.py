class Config:
    _name: str

    def __init__(self, name: str = "dev"):
        self._name = name

    @property
    def name(self) -> str:
        return self._name


app_config = Config()
