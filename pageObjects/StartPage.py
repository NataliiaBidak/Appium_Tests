from pageObjects.CreateAccount import CreateAccount
from utilities.BaseClass import BaseClass

class StartPage(BaseClass):


    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()






        # com.upside.consumer.android.beta: id / sign_up_password_text_tv
        # com.upside.consumer.android.beta: id / sign_up_clickable_tv
        # com.upside.consumer.android.beta: id / sign_up_password_stregth_progress_pb
        # com.upside.consumer.android.beta: id / sign_up_password_stregth_text_tv
        #
        # com.upside.consumer.android.beta: id / sign_up_password_requirements_title_tv
        # com.upside.consumer.android.beta: id / sign_up_password_requirements_min_characters_tv
        #
        # com.upside.consumer.android.beta: id / sign_up_password_requirements_one_letter_tv
        # com.upside.consumer.android.beta: id / sign_up_password_requirements_number_tv
        # com.upside.consumer.android.beta: id / sign_up_password_requirements_special_character_tv
    email_sign_up_button = "com.upside.consumer.android.beta:id/login_sing_up_email_b"

    def email_sign_up(self):
        self.log.info("Click on sign_up button")
        self.driver.find_element_by_id(StartPage.email_sign_up_button).click()
        return CreateAccount(self.driver)




