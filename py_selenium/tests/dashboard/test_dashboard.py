from os import path, remove

from py_selenium.helpers.file_helpers import compare_files_lines, compare_attributes, wait_until_file_exists
from py_selenium.helpers.screenshots import take_screenshot
from py_selenium.pages.dash_board_page import DashBoardPage
from py_selenium.tests.base_test import BaseTest


def get_actual_path(file_name):
    _this_dir = path.dirname(path.realpath(__file__))
    return path.realpath(path.join(_this_dir, file_name))


class TestDashboard(BaseTest):
    def nothing(self):
        pass

    def run_dashboard_test(self, browser, data, temp_dir, test_num):

        str_path_expected = self.get_path("dashboard/expected/export_" + str(test_num) + ".csv")

        dashboard = DashBoardPage(browser).open()
        take_screenshot(browser, "dashboard")

        dashboard.clear()

        dashboard.set_date(data.date)

        for transit in data.transits:
            dashboard.select_transit(transit)

        dashboard.search()

        dashboard.download_csv_1()
        files_match = self.downloaded_file_matches(temp_dir, str_path_expected)
        return files_match

    def downloaded_file_matches(self, temp_dir, expected):
        actual_excel_file = path.join(temp_dir, "export.csv")

        wait_until_file_exists(actual_excel_file)

        files_match = compare_files_lines(actual_excel_file, expected)
        if files_match:
            files_match = compare_attributes(actual_excel_file, expected,
                                             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16])

        remove(actual_excel_file)
        assert files_match
