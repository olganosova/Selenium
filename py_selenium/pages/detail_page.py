from selenium.webdriver.common.by import By

from py_selenium.helpers.wait_helper import wait_until_visible
from py_selenium.pages.tardis_base_page import TardisBasePage


class DetailPage(TardisBasePage):
    _book_dropdown_locator = (By.ID, 'iconBook')
    _filter_search_book_locator = (By.ID, 'txtSearchiconBook')
    _daily_pnl_total_locator = (By.ID, 'smryDailyPnlCde')
    _download_button_2_locator = (By.ID, 'btnDetailActualsCsv')
    _download_button_3_locator = (By.ID, 'btnDetailAttrCsv')

    def __init__(self, driver):
        super().__init__(driver)

    def download_csv_2(self):
        wait_until_visible(self.driver, self._download_button_locator, "unable to find first download button")
        wait_until_visible(self.driver, self._download_button_2_locator, "unable to find second download button")

        download_button = self.find_element(*self._download_button_2_locator)
        download_button.click()

    def download_csv_3(self):
        wait_until_visible(self.driver, self._download_button_3_locator, "unable to find third download button")

        download_button = self.find_element(*self._download_button_3_locator)
        download_button.click()

    def get_daily_pnl_total(self):
        wait_until_visible(self.driver, self._daily_pnl_total_locator, "unable to see numbers")
        return self.find_element(*(self._daily_pnl_total_locator)).text
