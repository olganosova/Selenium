import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.balance_sheet.test_balance_sheet import TestBalanceSheet


class TestBalanceSheet2(TestBalanceSheet):
    @pytest.mark.selenium
    @pytest.mark.skip(reason="Waiting for Ella to provide filters")
    def test_balance_sheet_2(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-07-26"
        data.transits = ["95307"]
        data.book = "ADMIN"
        data.parallel_mode = "true"

        return self.run_balance_sheet_test(browser, data, temp_dir)
