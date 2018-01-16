import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.balance_sheet.test_balance_sheet import TestBalanceSheet


class TestBalanceSheet1(TestBalanceSheet):
    @pytest.mark.selenium
    def test_balance_sheet_1(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-07-26"
        data.transits = ["95307"]
        data.book = "ADMIN"
        data.parallel_mode = "false"

        return self.run_balance_sheet_test(browser, data, temp_dir)
