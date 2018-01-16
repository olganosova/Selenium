from selenium.webdriver.common.by import By

from py_selenium.helpers.wait_helper import wait_until_visible
from py_selenium.pages.tardis_base_page import TardisBasePage


class NtcPage(TardisBasePage):
    _book_dropdown_locator = (By.ID, 'iconBook')
    _filter_search_book_locator = (By.ID, 'txtSearchiconBook')
    _download_button_locator = (By.ID, 'btnDetailAttrCsv')

    def download_csv(self, grid_number):
        self._download_button_locator = (By.ID, grid_number)
        wait_until_visible(self.driver, self._download_button_locator, "unable to find download button: " + grid_number)

        download_button = self.find_element(*self._download_button_locator)
        download_button.click()

    def __init__(self, driver):
        super().__init__(driver)
