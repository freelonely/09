from Selenium_test.lebo_shop.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from Selenium_test.lebo_shop.public.logging_method import LoggingMethod

class RegistePage(BasePage):
    username=(By.NAME,'username')
    email=(By.NAME,'email')
    password=(By.NAME,'password')
    confirmpwd=(By.NAME,'repassword')
    captcha=(By.NAME,'captcha')
    submit=(By.CLASS_NAME,'submit_reg')

    def input_username(self,username):
        self.input_text(self.username,username)

    def input_email(self,email):
        self.input_text(self.email,email)

    def input_password(self,password):
        self.input_text(self.password,password)

    def input_confirmpwd(self,confirmpwd):
        self.input_text(self.confirmpwd,confirmpwd)

    def input_captcha(self,captcha):
        self.input_text(self.captcha,captcha)
    def click_submit(self):
        self.click(self.submit)

