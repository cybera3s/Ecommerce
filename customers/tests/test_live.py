# import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
import os
from selenium.webdriver.common.by import By


class RegistrationLiveTest(StaticLiveServerTestCase):
    driver: WebDriver

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = WebDriver(os.getcwd() + '/chromedriver')
        cls.driver.implicitly_wait(20)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_register_success(self):
        self.driver.get(self.live_server_url + '/customers/register/')

        self.assertIn('Register', self.driver.title)

        username_input = self.driver.find_element(by=By.NAME, value="phone")
        username_input.send_keys('09987654321')

        email_input = self.driver.find_element(by=By.NAME, value="email")
        email_input.send_keys('live_test@email.com')

        gender_input = self.driver.find_element(by=By.NAME, value="gender")
        gender_input.send_keys('Male')

        password_input = self.driver.find_element(by=By.NAME, value="password")
        password_input.send_keys('123456789')

        confirm_password_input = self.driver.find_element(by=By.NAME, value="confirm_password")
        confirm_password_input.send_keys('123456789')

        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/form/input[2]').click()
        self.assertIn('Login', self.driver.title)
