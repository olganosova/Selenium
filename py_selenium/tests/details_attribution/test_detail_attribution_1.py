import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.detail_base_test import TestDetailBase


class TestDetailAttribution1(TestDetailBase):
    @pytest.mark.selenium
    def test_detail_attribution_1(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-03-31"
        data.transits = []
        data.book = "EQUITY"

        return self.run_detail_test(browser, data, temp_dir, 3)
