import pytest

from py_selenium.helpers.data_builder import DataBuilder
from py_selenium.tests.management_view.test_management_view import TestManagementView


class TestManagementView2(TestManagementView):
    @pytest.mark.selenium
    def test_management_view_2(self, temp_dir, browser):
        data = DataBuilder().get_default_data()

        data.date = "2017-03-31"

        return self.run_management_view_test(browser, data, temp_dir)
