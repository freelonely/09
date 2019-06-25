from HTMLTestRunner import HTMLTestRunner

import unittest
import time
test_case = "D:/09/my_api_test/haha/heihei"
report_dir = "D:/09/my_api_test/haha/reports"

discover = unittest.defaultTestLoader.discover(test_case,pattern="py_test01.py")

now = time.strftime("%y-%m-%d %H_%M_%S")
report_name = report_dir+"/"+now+"_test_report.html"

with open(report_name,"wb") as f:
    runner = HTMLTestRunner(stream=f,title="接口测试",description="test_report")
    runner.run(discover)
