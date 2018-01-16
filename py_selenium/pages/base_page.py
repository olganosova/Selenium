from pypom import Page

from py_selenium.helpers.config import get_config_value


class BasePage(Page):

    def __init__(self, driver):
        super().__init__(driver)

        self.base_url = get_config_value('base_url')
