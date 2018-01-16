from os import path

import pytest

from py_selenium.helpers.ApprovalLineEndingsPatcher import patch_approval_library_to_ignore_line_endings
from py_selenium.helpers.driver_builder import DriverBuilder
from py_selenium.helpers.screenshots import take_screenshot


class BaseTest(object):
    @pytest.fixture(autouse=True)
    def patch_approval_tests(self):
        """
        The approval tests library compares files including line endings.
        In order to be able to run this on Linux without worrying about line ending differences
        patch the approval tests library with own comparison.
        """
        patch_approval_library_to_ignore_line_endings()
        return

    def get_path(self, file_name):
        _this_dir = path.dirname(path.realpath(__file__))
        return path.realpath(path.join(_this_dir, file_name))

    @pytest.fixture(scope="function")
    def temp_dir(self, tmpdir):
        temp_dir = tmpdir.strpath
        print("Using temp dir:" + temp_dir)
        return temp_dir

    @pytest.fixture(scope="function")
    def browser(self, request, temp_dir):
        """
        Creates a browser object for every test
        method.
        Closes the browser afterwards.
        """

        def fin():
            if browser:
                print("taking final screenshot")
                take_screenshot(browser, "Test Finished")
                print("closing browser")
                browser.quit()
            else:
                print("browser is null?")

        request.addfinalizer(fin)

        browser = None   # assign browser so that don't error in fin() if not able to get browser
        browser = DriverBuilder().get_driver(download_location=temp_dir)

        return browser
