from pageObjects.CreateAccount import CreateAccount
from utilities.BaseClass import BaseClass


class StartPage(BaseClass):

    email_sign_up_button = "com.upside.consumer.android.beta:id/login_sing_up_email_b"

    def __init__(self, driver):
        self.driver = driver
        self.log = self.get_logger()

    def email_sign_up(self):
        self.log.info("Click on sign_up button")
        self.driver.find_element_by_id(StartPage.email_sign_up_button).click()
        return CreateAccount(self.driver)
