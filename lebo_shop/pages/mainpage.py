from Selenium_test.lebo_shop.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from Selenium_test.lebo_shop.public.logging_method import LoggingMethod

class MainPage(BasePage):
    # 首页登录按钮
    login_btn = (By.LINK_TEXT, u'登录')
    # 退出登录
    logout_btn = (By.LINK_TEXT, u'安全退出')
    # 登录后首页用户名显示
    login_str_location = (By.CLASS_NAME, 'loginfo')
    #免费注册按钮
    reg_btn=(By.LINK_TEXT,'免费注册')

    #首页点击登录，进入登录页
    def enter_loginpage(self):
        self.click(self.login_btn)

    # 退出
    def logout(self):
        self.click(self.logout_btn)

    # 获取用户信息
    def get_userinfo(self):
        return self.get_text(self.login_str_location)

    #判断是否登录成功
    def is_suc_login(self):
        if self.ele_is_visibility(self.logout_btn):
            return True
        else:
            return False

    def enter_reg(self):
        self.click(self.reg_btn)




