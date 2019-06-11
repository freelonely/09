import unittest
import os
# from Selenium_test.lebo_shop.cases.test_login import Test_Login
import HTMLTestRunner
import time

suite=unittest.TestSuite()
# suite.addTest(Test_Login('test_login'))
discover=unittest.defaultTestLoader.discover(start_dir=os.path.dirname(os.path.abspath('.'))+'\\cases',pattern='test*.py')
suite.addTest(discover)
# runner = unittest.TextTestRunner()
report_time=time.strftime('%Y-%m-%d_%H_%M_%S')
report_name=os.path.dirname(os.path.abspath('.'))+'\\report\\'+report_time+'.html'
f=open(report_name,'wb')#wb 二进制文件的写操作
runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='Test Report',description='null')
runner.run(suite)




