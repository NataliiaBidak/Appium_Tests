import pytest
from pageObjects.StartPage import StartPage
from utilities.BaseClass import BaseClass
from TestData import CreateAccountData


class TestHomePage(BaseClass):

    def test_sign_up(self, get_data):
        home_page = StartPage(self.driver)
        sign_up_page = home_page.email_sign_up()
        sign_up_page.type_email(get_data['email'], get_data['password'])
        assert sign_up_page.is_enabled_create_acc_btn() == get_data[
            'valid'], "Actual and Expected states of button don't match"

    @pytest.fixture(params=CreateAccountData.test_data, ids=[str(i) for i in CreateAccountData.test_data])
    def get_data(self, request):
        return request.param

    @pytest.fixture(autouse=True)
    def setup_teardown(self, request):
        self.get_logger().info('Test is started')

        def fin():
            self.driver.reset()

        request.addfinalizer(fin)
