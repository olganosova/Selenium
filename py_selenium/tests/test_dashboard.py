import json
from os import path, walk, remove
from os.path import join

import pytest

from py_selenium.helpers.file_helpers import compare_files_lines, wait_until_file_exists
from py_selenium.helpers.screenshots import take_screenshot
from py_selenium.pages.dash_board_page import DashBoardPage
from py_selenium.tests.base_test import BaseTest


class TestDashboard(BaseTest):
    @pytest.mark.selenium
    @pytest.mark.skip(reason="These tests have been re-written as seperate tests in dashboard folder")
    def test_dashboard_csv(self, temp_dir, browser):
        DashBoardPage(browser).open()
        take_screenshot(browser, "dashboard")

        assert (self.run_all_tests(browser, temp_dir))

    def run_all_tests(self, browser, temp_dir):
        all_tests_passed = True

        subdirs = [x[0] for x in walk(self.get_path("../../data/dashboard"))]
        inner_number = 0
        for subdir in subdirs:
            inner_number = int(inner_number) + 1
            if inner_number == 1:
                continue

            str_path_config = join(subdir, "data.json")
            str_path_expected = join(subdir, "export.csv")
            inner_config = self.parse_config(str_path_config)

            test_passed = self.run_test_from_config(browser, temp_dir, inner_config, str_path_expected,
                                                    inner_number - 1)
            if not test_passed:
                print("Failed test with config #" + str(inner_number - 1))
                all_tests_passed = False

        return all_tests_passed

    def run_test_from_config(self, browser, temp_dir, config, str_path_expected, config_number):
        dashboard = DashBoardPage(browser)

        dashboard.clear()
        dashboard.set_date(config['test_date'])

        for tran in config['transits']:
            dashboard.select_transit(tran)

        dashboard.search()

        dashboard.download_csv_1()

        files_match = self.downloaded_file_matches(temp_dir, str_path_expected)
        return files_match

    def get_path(self, file_name):
        _this_dir = path.dirname(path.realpath(__file__))
        return path.realpath(path.join(_this_dir, file_name))

    def parse_config(self, path_to_config):
        result = {'base_url': '', 'test_date': '', 'test_book': '', 'transits': [], 'parallel_mode': False}

        with open(path_to_config) as json_data:
            config = json.load(json_data)
            result['base_url'] = config['url']
            result['test_date'] = config['date']
            if 'book' in config:
                result['test_book'] = config['book']
            if 'transits' in config:
                result['transits'] = config['transits']
            result['parallel_mode'] = config['parallel_mode']
            json_data.close()
            return result

    def downloaded_file_matches(self, temp_dir, expected):
        actual_excel_file = path.join(temp_dir, "export.csv")

        wait_until_file_exists(actual_excel_file)

        # for dash board daysoutstanding changes each day, so we will count number of lines for now
        # TODO will use this method when define list of attributes to check
        files_match = compare_files_lines(actual_excel_file, expected)

        remove(actual_excel_file)
        return files_match
