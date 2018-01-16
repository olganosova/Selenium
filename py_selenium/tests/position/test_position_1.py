import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.position.test_position import TestPosition


class TestPosition1(TestPosition):
    @pytest.mark.selenium
    @pytest.mark.working
    def test_position_1(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-07-26"
        data.transits = []
        data.book = "COLVA"

        return self.run_position_test(browser, data, temp_dir, 1)
