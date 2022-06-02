import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from core.models import User
from django.conf import settings


CHROME_DRIVER_PATH = settings.CHROMEDRIVERPATH


class RegistrationLiveTest(StaticLiveServerTestCase):
    driver: WebDriver

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = WebDriver(CHROME_DRIVER_PATH)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_register_success(self):
        self.driver.get(self.live_server_url + reverse("customers:customer_register"))

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

        self.driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()

        self.assertIn('Login', self.driver.title)
        time.sleep(5)


class LoginLiveTest(StaticLiveServerTestCase):
    driver: WebDriver

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = WebDriver(CHROME_DRIVER_PATH)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_login_success(self):
        self.driver.get(self.live_server_url + reverse("customers:customer_login"))

        User.objects.create_user(email='test1@email.com', phone='09123456789', password='1234')

        self.assertIn('Login', self.driver.title)

        phone_input = self.driver.find_element(by=By.NAME, value="phone")
        phone_input.send_keys('09123456789')

        password_input = self.driver.find_element(by=By.NAME, value="password")
        password_input.send_keys('1234')

        self.driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
        time.sleep(5)