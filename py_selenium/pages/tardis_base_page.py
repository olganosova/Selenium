from selenium.webdriver.common.by import By

from py_selenium.helpers.config import get_config_value, get_config
from py_selenium.helpers.wait_helper import wait_until_visible
from py_selenium.pages.base_page import BasePage


class TardisBasePage(BasePage):
    _search_button_locator = (By.ID, 'btnSearchFilters')
    _clear_button_locator = (By.ID, 'btnClearFilters')
    _parallel_mode_locator = (By.ID, 'chkParallelMode')
    _transit_dropdown_locator = (By.ID, 'iconTransit')
    _transit_all_dcheckbox = (By.ID, 'chkAlliconTransit')

    _download_button_locator = (By.ID, 'summaryCsv')
    _pivot_1_checkbox_locator = (By.XPATH, '(//span[@label="Pivot Mode"])[1]')
    _pivot_2_checkbox_locator = (By.XPATH, '(//span[@label="Pivot Mode"])[2]')

    # moved to config.json
    # DOWNLOAD_BUTTON_WAIT = 60
    DOWNLOAD_BUTTON_WAIT_LONG = 240

    # base_url is loaded from data.json
    # base_url = "http://sdisvrba505.scglobaluat.aduat.scotiacapital.com:8181/success/s9"

    test_book = ""
    test_transit = ""
    test_date = ""
    parallel_mode = False

    def __init__(self, driver):
        super().__init__(driver)

        self.base_url = get_config_value('base_url')
        config = get_config()
        self.parallel_mode = config['parallel_mode']

    def clear(self):
        clear_button = self.find_element(*self._clear_button_locator)
        clear_button.click()

    def set_date(self, dte=None):
        date_element = self.find_element(By.NAME, "dp2")
        date_element.clear()
        if dte is None:
            date_element.send_keys(self.test_date + '\n')
        else:
            date_element.send_keys(dte + '\n')

    def select_book(self, test_book):
        book_dropdown = self.find_element(*self._book_dropdown_locator)
        book_dropdown.click()
        #
        checkbox_xpath = '//span[./text()="' + test_book + '"]'

        equity_checkbox = self.find_element(By.XPATH, checkbox_xpath)

        equity_checkbox.click()

    def select_transit(self, test_transit):
        transit_drop = self.find_element(*self._transit_dropdown_locator)

        transit_drop.click()

        checkbox_xpath = '//span[./text()="' + test_transit + '"]'

        transit_checkbox = self.find_element(By.XPATH, checkbox_xpath)

        transit_checkbox.click()
        transit_drop.click()

    def select_all_transits(self):
        transit_drop = self.find_element(*self._transit_dropdown_locator)

        transit_drop.click()

        checkbox_all_transits = self.find_element(*self._transit_all_dcheckbox)

        checkbox_all_transits.click()
        transit_drop.click()

    def select_parallel_mode(self):
        pm_checkbox = self.find_element(*self._parallel_mode_locator)
        pm_checkbox.click()

    def search(self):
        search_button = self.find_element(*self._search_button_locator)
        search_button.click()
        wait_until_visible(self.driver, self._download_button_locator, "unable to find first download button")

    def search_long(self):
        search_button = self.find_element(*self._search_button_locator)
        search_button.click()
        wait_until_visible(self.driver, self._download_button_locator, "unable to find first download button",
                           wait_in_seconds=self.DOWNLOAD_BUTTON_WAIT_LONG)

    def search_no_wait(self):
        search_button = self.find_element(*self._search_button_locator)
        search_button.click()

    def download_csv_1(self):
        wait_until_visible(self.driver, self._download_button_locator, "unable to find first download button")

        download_button = self.find_element(*self._download_button_locator)
        download_button.click()

    def download_csv_1_long(self):
        wait_until_visible(self.driver, self._download_button_locator, "unable to find first download button",
                           wait_in_seconds=self.DOWNLOAD_BUTTON_WAIT_LONG)

        download_button = self.find_element(*self._download_button_locator)
        download_button.click()

    def search_for_book(self, data):
        self.clear()
        self.set_date(data.date)
        self.select_book(data.book)

        if data.parallel_mode.lower() == 'true':
            self.select_parallel_mode()

        self.search()

    def unpivot_grid(self, grid_number):
        pivot_locator = self._pivot_1_checkbox_locator
        if grid_number > 1:
            pivot_locator = self._pivot_2_checkbox_locator

        wait_until_visible(self.driver, pivot_locator, "unable to find pivot checkbox number " + str(grid_number),
                           wait_in_seconds=120)

        pivot_checkbox = self.find_element(*pivot_locator)

        pivot_checkbox.click()
