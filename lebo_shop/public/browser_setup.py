from selenium import webdriver
from Selenium_test.lebo_shop.public.logging_method import LoggingMethod
from Selenium_test.lebo_shop.public.ReadConfig import readconfig

class BrowserSetUp():
    def __init__(self,logger):
        self.logger=logger
        self.browsername=readconfig('browser','browserName',logger)
        self.driver=''
        self.get_driver=True
    def browser_setup(self):
        if self.browsername.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browsername.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browsername.lower() == 'ie':
            self.driver=webdriver.Ie()
        else:
            self.get_driver=False
            self.logger.error('传入的浏览器名称有误')

        if self.get_driver:
            return self.driver
        else:
            return self.get_driver
