from appium import webdriver
import allure
import time
import os
import subprocess
import pytest
from ..settings import *

driver = None


@pytest.fixture(scope="class")
def setup(request):
    desired_caps = DESIRED_CAPS
    global driver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def report():
    if os.listdir(TEST_REPORTS):
        filelist = [f for f in os.listdir(TEST_REPORTS)]
        for f in filelist:
            os.remove(os.path.join(TEST_REPORTS, f))
    assert not os.listdir(TEST_REPORTS)
    yield
    if RUN_REPORT_AUTOMATICALLY:
        time.sleep(10)
        subprocess.Popen("allure serve {}".format(TEST_REPORTS), shell=True, cwd=PROJECT_FOLDER)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    rep = outcome.get_result()
    if (rep.when == 'call' or rep.when == 'setup') and (rep.failed or rep.skipped):
        try:
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot_captured',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print('Fail to take screenshot'.format(e))
