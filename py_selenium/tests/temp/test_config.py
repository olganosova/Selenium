import pytest

from py_selenium.helpers.config import is_headless


class TestConfig():
    '''
    This is a temporary test just to ensure jenkins is running tests correctly
    '''

    @pytest.mark.unit
    def test_config(self):
        assert (is_headless() == True or is_headless() == False)
