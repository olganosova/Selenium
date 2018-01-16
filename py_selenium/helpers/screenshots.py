import time

from os import path, makedirs


def take_screenshot(browser, description=""):
    base_name = _get_screenshot_base_name(_create_screenshot_directory(), description)

    _create_screenshot(browser, base_name)

    _write_page_source(browser.page_source, base_name)


def _create_screenshot_directory():
    this_dir = path.dirname(path.realpath(__file__))
    screenshot_dir = path.realpath(path.join(this_dir, "../../screenshots"))
    if not path.exists(screenshot_dir):
        makedirs(screenshot_dir)
    return screenshot_dir


def _create_screenshot(browser, base_name):
    name = base_name + ".png"
    print("saving screenshot to: " + name)
    screenshot_success = browser.save_screenshot(name)
    if not screenshot_success:
        print("Unable to take screenshot! " + name)


def _write_page_source(page_source, base_name):
    text_file = open(base_name + ".html", "w", encoding="utf-8")
    text_file.write(page_source)
    text_file.close()


def _get_screenshot_base_name(screenshot_dir, description):
    return path.join(screenshot_dir, time.strftime("%Y%m%d-%H%M%S") + "-" + description)
