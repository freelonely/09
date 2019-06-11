import time
import os

class Screenshot():
    def __init__(self,driver):
        self.driver=driver

    def screenshot(self,str):
        scr_time=time.strftime('%Y-%m-%d_%H_%M_%S')
        scr_name=os.path.dirname(os.path.abspath('.'))+'\\screenshot\\'+scr_time+'_'+str+'.png'
        self.driver.get_screenshot_as_file(scr_name)

