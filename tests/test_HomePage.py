
import pytest
from time import sleep
#from TestData.HomePageData import HomePageData
from pageObjects.StartPage import StartPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_sign_up(self):

        home_page=StartPage(self.driver)
        sign_up_page = home_page.email_sign_up()
        sign_up_page.type_email("fccvbvnirama@gmail.com", "AAA")
        sign_up_page.is_enabled_create_acc_btn()

        sleep(10)
    #     log.info("first name is "+getData["firstname"])
    #     homepage.getName().send_keys(getData["firstname"])
    #     homepage.getEmail().send_keys(getData["lastname"])
    #     homepage.getCheckBox().click()
    #     self.selectOptionByText(homepage.getGender(), getData["gender"])
    #
    #     homepage.submitForm().click()
    #
    #     alertText = homepage.getSuccessMessage().text
    #
    #     assert ("Success" in alertText)
    #     self.driver.refresh()
    #
    # @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    # def getData(self, request):
    #     return request.param

