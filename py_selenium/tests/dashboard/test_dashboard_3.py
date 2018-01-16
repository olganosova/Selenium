from os import path

import pytest
from approvaltests import verify
from approvaltests.reporters import GenericDiffReporterFactory

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.helpers.file_helpers import wait_until_file_exists
from py_selenium.helpers.screenshots import take_screenshot
from py_selenium.pages.dash_board_page import DashBoardPage
from py_selenium.tests.dashboard.test_dashboard import TestDashboard


class TestDashboard1(TestDashboard):
    @pytest.mark.selenium
    def test_dashboard_3(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-03-31"
        data.transits = ["95307"]

        dashboard = DashBoardPage(browser).open()
        take_screenshot(browser, "dashboard")

        dashboard.clear()

        dashboard.set_date(data.date)

        for transit in data.transits:
            dashboard.select_transit(transit)

        dashboard.search()

        dashboard.download_csv_1()

        actual_file = path.realpath(path.join(temp_dir, "export.csv"))
        wait_until_file_exists(actual_file)

        data = "sfsdfsdf\ndfsdsdf\nsdfsdfsdfs\n"

        self.reporter = GenericDiffReporterFactory().get_first_working()
        verify(data)
