from os import path

from approvaltests import verify_file
from approvaltests.reporters import GenericDiffReporterFactory

from py_selenium.helpers.file_helpers import wait_until_file_exists
from py_selenium.helpers.screenshots import take_screenshot
from py_selenium.pages.dash_board_page import DashBoardPage
from py_selenium.tests.base_test import BaseTest


def get_actual_path(file_name):
    _this_dir = path.dirname(path.realpath(__file__))
    return path.realpath(path.join(_this_dir, file_name))


class TestDetailBase(BaseTest):
    def nothing(self):
        pass

    def run_detail_test(self, browser, data, temp_dir, grid_number):
        dashboard = DashBoardPage(browser).open()
        take_screenshot(browser, "dashboard")

        detail_tab = dashboard.select_detail_tab()
        take_screenshot(browser, "detail_tab_before_search_grid_" + str(grid_number))

        # for transit in data.transits:
        #   dashboard.select_transit(transit)

        detail_tab.search_for_book(data)
        take_screenshot(browser, "detail_tab_after_search_grid_" + str(grid_number))

        # unpivot only for 2-nd and 3-rd grids
        if grid_number != 1:
            detail_tab.unpivot_grid(grid_number - 1)

        if grid_number == 1:
            detail_tab.download_csv_1()
        elif grid_number == 2:
            detail_tab.download_csv_2()
        else:
            detail_tab.download_csv_3()

        actual_file = path.realpath(path.join(temp_dir, "export.csv"))
        wait_until_file_exists(actual_file)
        self.reporter = GenericDiffReporterFactory().get_first_working()
        verify_file(actual_file)
