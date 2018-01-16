from selenium.webdriver.common.by import By

from py_selenium.pages.balance_sheet_page import BalanceSheetPage
from py_selenium.pages.detail_page import DetailPage
from py_selenium.pages.management_view_page import ManagementViewPage
from py_selenium.pages.ntc_page import NtcPage
from py_selenium.pages.position_page import PositionPage
from py_selenium.pages.tardis_base_page import TardisBasePage


class DashBoardPage(TardisBasePage):
    _transit_dropdown_locator = (By.ID, 'iconTransit')

    _detail_tab_locator = (By.ID, 'mnuDetail')
    _bs_tab_locator = (By.ID, 'mnuBalanceSheet')
    _position_tab_locator = (By.ID, 'mnuRiskAttr')
    _balance_sheet_tab_locator = (By.ID, 'mnuBalanceSheet')
    _management_view_tab_locator = (By.ID, 'mnuManagementView')
    _ntc_view_tab_locator = (By.ID, 'mnuNTC')

    def __init__(self, driver):
        super().__init__(driver)

    def select_detail_tab(self) -> DetailPage:
        detail_tab = self.find_element(*self._detail_tab_locator)
        detail_tab.click()
        return DetailPage(self.driver)

    def select_position_tab(self) -> PositionPage:
        position_tab = self.find_element(*self._position_tab_locator)
        position_tab.click()
        return PositionPage(self.driver)

    def select_balance_sheet_tab(self) -> BalanceSheetPage:
        balance_sheet_tab = self.find_element(*self._balance_sheet_tab_locator)
        balance_sheet_tab.click()
        return BalanceSheetPage(self.driver)

    def select_ntc_tab(self) -> NtcPage:
        ntc_tab = self.find_element(*self._ntc_view_tab_locator)
        ntc_tab.click()
        return NtcPage(self.driver)

    def select_management_view_tab(self) -> ManagementViewPage:
        management_view_tab = self.find_element(*self._management_view_tab_locator)
        management_view_tab.click()
        return ManagementViewPage(self.driver)
