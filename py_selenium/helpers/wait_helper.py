from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from py_selenium.helpers import config


def wait_until_visible(driver, locator, msg="", wait_in_seconds=config.wait_time()):
    WebDriverWait(driver, wait_in_seconds).until(
        expected_conditions.visibility_of_element_located(locator),
        msg
    )
