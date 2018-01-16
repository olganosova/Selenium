import json

from os import path


def _get_path(file_name):
    _this_dir = path.dirname(path.realpath(__file__))
    return path.realpath(path.join(_this_dir, file_name))


def _load_config():
    path_to_config = _get_path("../../config/config.json")
    with open(path_to_config) as json_data:
        config = json.load(json_data)
        json_data.close()
        return config


def get_config():
    # could cache config
    return _load_config()


def get_config_value(key):
    return _load_config()[key]


def is_headless():
    return get_config_value("headless").lower() == "true"


def get_chromedriver_logging_on():
    return get_config_value("chromedriver_logging_on").lower() == "true"

def wait_time():
    return int(get_config_value("wait_time"))