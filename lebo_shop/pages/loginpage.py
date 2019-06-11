from Selenium_test.lebo_shop.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from Selenium_test.lebo_shop.public.logging_method import LoggingMethod

class LoingPage(BasePage):
    # 用户名输入框
    username = (By.NAME, 'login_info')
    # 密码输入框
    password = (By.NAME, 'password')
    # 登录按钮
    submit = (By.CLASS_NAME, 'submit_login')
    # 登录失败的文字提示
    errorlogin_location = (By.CLASS_NAME, 'prompt')

    # 输入用户名
    def input_username(self, name):
        self.input_text(self.username, name)

    # 输入密码
    def input_password(self, pwd):
        self.input_text(self.password, pwd)

    # 点击登录按钮，提交表单
    def click_submit(self):
        self.click(self.submit)
    #是否登录成功
    # def is_logined(self):

    # 获取登录失败文案
    def get_errorlogin_str(self):
        return self.get_text(self.errorlogin_location)


