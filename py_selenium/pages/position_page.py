from selenium.webdriver.common.by import By

from py_selenium.helpers.wait_helper import wait_until_visible
from py_selenium.pages.tardis_base_page import TardisBasePage


class PositionPage(TardisBasePage):
    _book_dropdown_locator = (By.ID, 'iconBook')
    _filter_search_book_locator = (By.ID, 'txtSearchiconBook')
    _pivot_1_first_value = (By.XPATH, '(//span[@class="ag-group-value"])[1]')
    _download_button_2_locator = (By.ID, 'btnPivot2Csv')

    def __init__(self, driver):
        super().__init__(driver)

    def download_csv_2(self):
        wait_until_visible(self.driver, self._download_button_2_locator, "unable to find second download button")

        download_button = self.find_element(*self._download_button_2_locator)
        download_button.click()

    def load_second_grid(self):
        first_row = self.find_element(*self._pivot_1_first_value)
        first_row.click()
        wait_until_visible(self.driver, self._download_button_2_locator, "unable to find second grid download button")
