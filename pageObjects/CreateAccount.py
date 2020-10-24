from utilities.BaseClass import BaseClass
from distutils.util import strtobool


class CreateAccount(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()
    sign_up_email_text = "com.upside.consumer.android.beta:id/sign_up_email_edit_et"
    create_account_btn = "com.upside.consumer.android.beta:id/sign_up_email_b"
    sign_up_password_text = "com.upside.consumer.android.beta:id/sign_up_password_edit_et"



    def type_email(self, email=None, password=None):
        self.log.info("Type email = {}, password ={}".format(email,password))
        self.driver.find_element_by_id(CreateAccount.sign_up_email_text).send_keys(email)
        self.driver.find_element_by_id(CreateAccount.sign_up_password_text).send_keys(password)

    def is_enabled_create_acc_btn(self):
        state = self.driver.find_element_by_id(CreateAccount.create_account_btn).get_attribute('enabled')
        self.log.info("Create account is enabled: {}".format(state))
        return bool(strtobool(state))
