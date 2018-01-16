from os import path

from approvaltests import verify_file
from approvaltests.reporters import GenericDiffReporterFactory

from py_selenium.helpers.file_helpers import wait_until_file_exists
from py_selenium.helpers.screenshots import take_screenshot
from py_selenium.pages.dash_board_page import DashBoardPage
from py_selenium.tests.base_test import BaseTest


class TestPosition(BaseTest):
    def nothing(self):
        pass

    def run_position_test(self, browser, data, temp_dir, grid_number):

        dashboard = DashBoardPage(browser).open()
        take_screenshot(browser, "dashboard")

        position_tab = dashboard.select_position_tab()
        take_screenshot(browser, str(grid_number) + " grid. position_tab_before_search")

        position_tab.clear()

        position_tab.set_date(data.date)

        if len(data.transits) == 1 and data.transits[0] == 'all':
            position_tab.select_all_transits()
        else:
            for transit in data.transits:
                position_tab.select_transit(transit)

        if data.book != "":
            position_tab.select_book(data.book)

        if data.parallel_mode.lower() == 'true':
            position_tab.select_parallel_mode()

        dashboard.search_long()

        take_screenshot(browser, str(grid_number) + " grid. position_tab__after_search")

        if grid_number == 2:
            position_tab.load_second_grid()

        position_tab.unpivot_grid(grid_number)

        if grid_number == 1:
            position_tab.download_csv_1()
        elif grid_number == 2:
            position_tab.download_csv_2()

        actual_file = path.realpath(path.join(temp_dir, "export.csv"))
        wait_until_file_exists(actual_file)
        self.reporter = GenericDiffReporterFactory().get_first_working()
        verify_file(actual_file)
