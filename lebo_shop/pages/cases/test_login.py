from Selenium_test.lebo_shop.pages.loginpage import LoingPage
from Selenium_test.lebo_shop.pages.mainpage import MainPage
from Selenium_test.lebo_shop.public.logging_method import LoggingMethod
from Selenium_test.lebo_shop.public.excel_method import ExcelMethod
from Selenium_test.lebo_shop.public.screenshot import Screenshot
from Selenium_test.lebo_shop.public.browser_setup import BrowserSetUp
import os
import sys
import unittest

class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = LoggingMethod('Test_Login').getlogger()
        cls.logger.info('创建driver对象')
        cls.driver = BrowserSetUp(cls.logger).browser_setup()
        url = 'http://106.13.46.164:8080/iwebshop/'
        cls.loginpage = LoingPage(cls.driver,cls.logger)
        cls.logger.info('打开商城首页')
        cls.loginpage.open_url(url)
        cls.mainpage=MainPage(cls.driver,cls.logger)
        cls.excelmethod=ExcelMethod(cls.logger)
        data_path = os.path.dirname(os.path.abspath('.')) + '\\data'+'\\login.xlsx'
        cls.logger.info(('读取测试用例',data_path))
        cls.user_list=cls.excelmethod.readExcel(data_path)
        cls.scr=Screenshot(cls.driver)
        cls.scr.screenshot(__class__.__name__ + '-' + sys._getframe().f_code.co_name)

    def test_login(self):
        self.logger.info(u'点击登录，进入登录页面')
        self.mainpage.enter_loginpage()
        self.scr.screenshot(__class__.__name__ + '-' + sys._getframe().f_code.co_name)
        for i in range(1,len(self.user_list)):
            # 输入用户名
            self.logger.info('输入用户名')
            self.loginpage.input_username(self.user_list[i][0])
            # 输入密码
            self.logger.info('输入密码')
            self.loginpage.input_password(self.user_list[i][1])
            # 单击登录按钮
            self.logger.info('点击登录按钮')
            self.loginpage.click_submit()
            self.scr.screenshot(__class__.__name__ + '-' + sys._getframe().f_code.co_name)

            if self.mainpage.is_suc_login():
                if self.user_list[i][0] in self.mainpage.get_userinfo():
                    self.excelmethod.saveExcel(i + 1, u'pass')
                    self.logger.info(u'退出登录')
                    self.mainpage.logout()
                    self.scr.screenshot(__class__.__name__ + '-' + sys._getframe().f_code.co_name)
                else:
                    self.excelmethod.saveExcel(i + 1, 'fail')
                    self.logger.error(u'第 %s 行用例执行失败' % (i + 1))
                    self.scr.screenshot(__class__.__name__ + '-' + sys._getframe().f_code.co_name)
            else:
                if self.loginpage.get_errorlogin_str() == self.user_list[i][2]:
                    self.excelmethod.saveExcel(i + 1, u'pass')
                    self.scr.screenshot(__class__.__name__ + '-' + sys._getframe().f_code.co_name)
                else:
                    self.excelmethod.saveExcel(i + 1, 'fail')
                    self.logger.error(u'第 %s 行用例执行失败' % (i + 1))
                    self.scr.screenshot(__class__.__name__ + '-' + sys._getframe().f_code.co_name)

    @classmethod
    def tearDownClass(cls):
        cls.logger.info(u'即将退出......')
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()
