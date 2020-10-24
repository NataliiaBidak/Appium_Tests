import pytest
from appium import webdriver
import time

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11.0",
        "deviceName": "Pixel_3a_API_30_x86",
        "autoGrantPermissions": "true",
        "app": "/home/nbidak/Downloads/app-betabs-debug.apk"
        # "appPackage": "com.upside.consumer.android.beta",
    #    "appActivity": "com.upside.consumer.android.beta.com.upside.consumer.android.activities.MainActivity"

    }
    driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)
