from os import path

from approvaltests import verify_file
from approvaltests.reporters import GenericDiffReporterFactory

from py_selenium.helpers.file_helpers import wait_until_file_exists
from py_selenium.helpers.screenshots import take_screenshot
from py_selenium.pages.dash_board_page import DashBoardPage
from py_selenium.tests.base_test import BaseTest


class TestNtc(BaseTest):
    def nothing(self):
        pass

    def run_ntc_test(self, browser, data, temp_dir, grid_number):

        dashboard = DashBoardPage(browser).open()
        take_screenshot(browser, "dashboard")

        ntc_tab = dashboard.select_ntc_tab()
        take_screenshot(browser, "NTC_tab_before_search")

        ntc_tab.clear()

        ntc_tab.set_date(data.date)

        if len(data.transits) == 1 and data.transits[0] == 'all':
            ntc_tab.select_all_transits()
        else:
            for transit in data.transits:
                ntc_tab.select_transit(transit)

        if data.book != "":
            ntc_tab.select_book(data.book)

        if data.parallel_mode.lower() == 'true':
            ntc_tab.select_parallel_mode()

        dashboard.search_no_wait()

        take_screenshot(browser, "NTC_tab_after_search")

        ntc_tab.download_csv(grid_number)

        actual_file = path.realpath(path.join(temp_dir, "export.csv"))
        wait_until_file_exists(actual_file)
        self.reporter = GenericDiffReporterFactory().get_first_working()
        verify_file(actual_file)
