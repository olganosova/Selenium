from selenium.webdriver.common.by import By

from py_selenium.pages.tardis_base_page import TardisBasePage


class BalanceSheetPage(TardisBasePage):
    _book_dropdown_locator = (By.ID, 'iconBook')
    _filter_search_book_locator = (By.ID, 'txtSearchiconBook')

    def __init__(self, driver):
        super().__init__(driver)
