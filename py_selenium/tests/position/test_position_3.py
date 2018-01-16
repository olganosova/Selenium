import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.position.test_position import TestPosition


class TestPosition3(TestPosition):
    @pytest.mark.selenium
    @pytest.mark.skip(reason="Filter is very big")
    def test_position_3(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-07-05"
        data.transits = ["all"]
        data.book = ""

        return self.run_position_test(browser, data, temp_dir, 1)
