import os
import sys

from selenium.webdriver import Chrome, PhantomJS, Firefox
from selenium.webdriver.chrome import webdriver as chrome_webdriver

from py_selenium.helpers import config


class DriverBuilder():
    def get_driver(self, download_location=None):

        driver = self.get_chrome_driver(download_location, config.is_headless(), config.get_chromedriver_logging_on())

        driver.set_window_size(1400, 900)

        return driver

    def get_chrome_driver(self, download_location, headless, chromedriver_logging_on):
        chrome_options = chrome_webdriver.Options()
        if download_location:
            prefs = {'download.default_directory': download_location,
                     'download.prompt_for_download': False,
                     'download.directory_upgrade': True,
                     'safebrowsing.enabled': False,
                     'safebrowsing.disable_download_protection': True}

            chrome_options.add_experimental_option('prefs', prefs)

        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox") # required to run in docker (?)

        driver_path = self.get_chromedriver_path()

        if chromedriver_logging_on:
            print("Loading ChromeDriver with logging on")
            service_args = ["--verbose", "--log-path=./chromedriver.log"]
        else:
            service_args = None

        print("Loading ChromeDriver from path:" + driver_path)

        driver = Chrome(executable_path=driver_path, chrome_options=chrome_options, service_args=service_args)

        if headless:
            self.enable_download_in_headless_chrome(driver, download_location)

        return driver

    def get_chromedriver_path(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        driver_path = os.path.abspath(os.path.join(dir_path, "../../drivers/chromedriver"))
        if sys.platform.startswith("win"):
            driver_path += ".exe"
        return driver_path

    def enable_download_in_headless_chrome(self, browser, download_dir):
        """
        there is currently a "feature" in chrome where
        headless does not allow file download: https://bugs.chromium.org/p/chromium/issues/detail?id=696481
        This method is a hacky work-around until the official chromedriver support for this.
        Requires chrome version 62.0.3196.0 or above.
        """

        # add missing support for chrome "send_command"  to selenium webdriver
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        browser.execute("send_command", params)

    def get_phantom_js(self, download_location):
        driver = PhantomJS()
        return driver

    def get_firefox(self, download_location, headless):
        driver = Firefox(firefox_binary="C:\Program Files\Mozilla Firefox\firefox.exe",
                         executable_path="C:\\Users\\sbutton\\projects\\python_selenium\\drivers\\geckodriver.exe")
        return driver
