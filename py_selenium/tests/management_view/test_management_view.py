from os import path

from approvaltests import verify_file
from approvaltests.reporters import GenericDiffReporterFactory

from py_selenium.helpers.file_helpers import wait_until_file_exists
from py_selenium.helpers.screenshots import take_screenshot
from py_selenium.pages.dash_board_page import DashBoardPage
from py_selenium.tests.base_test import BaseTest


class TestManagementView(BaseTest):
    def nothing(self):
        pass

    def run_management_view_test(self, browser, data, temp_dir):
        dashboard = DashBoardPage(browser).open()
        take_screenshot(browser, "dashboard")

        management_view_tab = dashboard.select_management_view_tab()
        take_screenshot(browser, "Management_View_tab_before_search")

        management_view_tab.set_date(data.date)
        management_view_tab = dashboard.select_management_view_tab()

        take_screenshot(browser, "Management_View_tab__after_search")

        management_view_tab.download_csv_1_long()

        actual_file = path.realpath(path.join(temp_dir, "management-report.csv"))
        wait_until_file_exists(actual_file)
        self.reporter = GenericDiffReporterFactory().get_first_working()
        verify_file(actual_file)
