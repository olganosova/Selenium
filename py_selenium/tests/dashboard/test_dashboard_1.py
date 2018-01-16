import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.dashboard.test_dashboard import TestDashboard


class TestDashboard1(TestDashboard):
    @pytest.mark.selenium
    def test_dashboard_1(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-03-31"
        data.transits = ["15263", "85647"]

        return self.run_dashboard_test(browser, data, temp_dir, 1)
