import os
from os import path

import pytest

from py_selenium.helpers.driver_builder import DriverBuilder


class TestJenkins():
    '''
    This is a temporary test just to ensure jenkins is running tests correctly
    '''

    @pytest.mark.skip(reason="Only for jenkins test")
    def test_jenkins(self):

        this_dir = path.dirname(path.realpath(__file__))
        file_name = path.realpath(path.join(this_dir, "../../../chromedriver.log"))

        with open(file_name) as f:
            lines = f.readlines()
            for line in lines:
                print(line)

        assert False == True

    @pytest.mark.skip(reason="Only for jenkins test")
    def test_find_chromedriver(self):

        root_dir = path.realpath("/")

        found = False
        for folder, subs, files in os.walk(root_dir):
            for filename in files:
                # print(folder + ":" + filename)
                if filename == "chromedriver.log":
                    print("!!!!!!!!!!!!!! chromedriver found!  " + folder + ":" + filename)
                    found = True

        if not found:
            print("chromedriver not found!")

        assert False == True

    @pytest.mark.skip(reason="Only for jenkins test")
    def test_run_chromedriver_directly(self):

        path = DriverBuilder().get_chromedriver_path()

        import subprocess
        print("Calling ChromeDriver")
        subprocess.call(path)

        print("ldd -v")
        subprocess.call("ldd -v " + path)

        print("ldd -d")
        subprocess.call("ldd -d " + path)
        # subprocess.call(["C:\\Program Files\\7-Zip\\7z.exe"])

        assert False == True

