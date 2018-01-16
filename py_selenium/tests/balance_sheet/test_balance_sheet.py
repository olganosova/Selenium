from os import path

from approvaltests import verify_file
from approvaltests.reporters import GenericDiffReporterFactory

from py_selenium.helpers.file_helpers import wait_until_file_exists
from py_selenium.helpers.screenshots import take_screenshot
from py_selenium.pages.dash_board_page import DashBoardPage
from py_selenium.tests.base_test import BaseTest


class TestBalanceSheet(BaseTest):
    def nothing(self):
        pass

    def run_balance_sheet_test(self, browser, data, temp_dir):

        dashboard = DashBoardPage(browser).open()
        take_screenshot(browser, "dashboard")

        balance_sheet_tab = dashboard.select_balance_sheet_tab()
        take_screenshot(browser, "Balance_sheet_tab_before_search")

        balance_sheet_tab.clear()

        balance_sheet_tab.set_date(data.date)

        for transit in data.transits:
            balance_sheet_tab.select_transit(transit)

        balance_sheet_tab.select_book(data.book)

        if data.parallel_mode.lower() == 'true':
            balance_sheet_tab.select_parallel_mode()

        dashboard.search()

        take_screenshot(browser, "Balance_sheet_tab__after_search")

        balance_sheet_tab.unpivot_grid(1)

        balance_sheet_tab.download_csv_1()

        actual_file = path.realpath(path.join(temp_dir, "export.csv"))
        wait_until_file_exists(actual_file)
        self.reporter = GenericDiffReporterFactory().get_first_working()
        verify_file(actual_file)
