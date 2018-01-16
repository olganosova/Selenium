import json
from os import path

from py_selenium.helpers.data import Data


class DataBuilder:
    test_data = Data()

    def __init__(self):
        data_file = self._get_path("../../data/default_data.json")
        self._load_data(data_file)

    def _get_path(self, file_name):
        _this_dir = path.dirname(path.realpath(__file__))
        return path.realpath(path.join(_this_dir, file_name))

    def _load_data(self, data_file):
        with open(data_file) as json_data:
            data = json.load(json_data)

            test_data = self.test_data

            if "transits" in data:
                test_data.transits = data["transits"]

            if "book" in data:
                test_data.book = data["book"]

            if "date" in data:
                test_data.date = data["date"]

            if "parallel_mode" in data:
                test_data.parallel_mode = data["parallel_mode"]

            json_data.close()

    def get_default_data(self):
        return self.test_data
