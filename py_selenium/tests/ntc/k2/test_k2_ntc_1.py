import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.ntc.test_ntc import TestNtc


class TestK2Ntc1(TestNtc):
    @pytest.mark.selenium
    def test_k2_ntc_1(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-07-26"
        data.transits = ["all"]
        data.book = ""

        return self.run_ntc_test(browser, data, temp_dir, 'grid_0')
