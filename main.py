from models import Review
from service import service_provider

if __name__ == '__main__':
    service_provider = service_provider
    f_reader = service_provider.file_reader()
    qt_bots = [f_reader.read_txt("qt_bots.txt").split("\n")]
    data = f_reader.read_json("test2.json")
    data_modes = [Review(**d) for d in data]
    # data = f_reader.read_json("qt_2017-01-01.json")

    a = 10
