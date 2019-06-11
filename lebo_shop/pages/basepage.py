from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self,driver,logger):
        self.driver=driver
        self.logger=logger
        self.timeout=10

    #判断元素是否存在
    def ele_is_presence(self,locator):
        try:
            ele=WebDriverWait(self.driver,self.timeout).until(EC.presence_of_element_located(locator))
            return ele
        # return self.driver.find_element(*locator)
        except:
            self.logger.error((u'ele_is_presence：未找到元素',locator))

    #发送文本
    def input_text(self,locator,text):
        try:
            self.ele_is_presence(locator).send_keys(text)
        except AttributeError:
            self.logger.error((locator,u'input_text：未找到元素或元素不可输入文本'))

    #点击操作
    def click(self,locator):
        try:
            self.ele_is_presence(locator).click()
        except AttributeError:
            self.logger.error((u'click：未找到元素或元素不可点击',locator))

    #打开url
    def open_url(self,url='http://106.13.46.164:8080/iwebshop/'):
        self.driver.get(url)

    # 获取文案
    def get_text(self, locator):
        try:
            return self.ele_is_presence(locator).text
        except AttributeError:
            self.logger.error((u'get_text:未找到元素或元素没有text属性',locator))

    # 元素是否可见（单个元素）
    def ele_is_visibility(self, locator):
        try:
            ele = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return ele
        except:
            self.logger.error(u'ele_is_visibility:未找到元素'+str(locator))

    # # 其他方法：
    # # 元素是否可见，返回list
    # def eles_is_visibility(self, *locator):
    #     try:
    #         ele = WebDriverWait(self.driver, self.timeout).until(\
    #             EC.visibility_of_all_elements_located(*locator))
    #         return ele
    #     except:
    #         self.src.screenshot()
    #         self.logger.error(u'%s元素不可见' % locator)
    #
    # # 元素不可见
    # def ele_isnot_visibility(self, *locator):
    #     try:
    #         status = WebDriverWait(self.driver, self.timeout).until( \
    #             EC.invisibility_of_element_located(*locator))
    #         return status
    #     except:
    #         self.src.screenshot()
    #         self.logger.error(u'%s元素依然可见' % locator)
