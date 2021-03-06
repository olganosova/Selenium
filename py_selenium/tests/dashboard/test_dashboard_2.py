import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.dashboard.test_dashboard import TestDashboard


class TestDashboard2(TestDashboard):
    @pytest.mark.selenium
    def test_dashboard_2(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-07-26"
        data.transits = ["85647"]

        self.run_dashboard_test(browser, data, temp_dir, 2)
