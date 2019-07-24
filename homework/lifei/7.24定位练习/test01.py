#   Date: 2019/7/21 0021
#   Name: life
#  _*_ coding:UTF-8  _*_

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# url = "file:///E:/%E4%B9%90%E6%90%8Fpython%E8%87%AA%E5%8A%A8%E5%8C%96/python%E8%87%AA%E5%8A%A8%E5%8C%96%EF%BC%88%E5%BC%80%E8%AF%BE%E5%89%8D%E5%AE%89%E8%A3%85%EF%BC%89/%E5%A5%BD%E5%A8%81%E8%80%81%E5%B8%88%E4%B8%8A%E8%AF%BE%E4%BB%A3%E7%A0%81/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%B3%A8%E5%86%8CA.html"
# 这个页面有多个iframe
url="file:///E:/%E4%B9%90%E6%90%8Fpython%E8%87%AA%E5%8A%A8%E5%8C%96/python%E8%87%AA%E5%8A%A8%E5%8C%96%EF%BC%88%E5%BC%80%E8%AF%BE%E5%89%8D%E5%AE%89%E8%A3%85%EF%BC%89/%E5%A5%BD%E5%A8%81%E8%80%81%E5%B8%88%E4%B8%8A%E8%AF%BE%E4%BB%A3%E7%A0%81/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)

# username = driver.find_element_by_id("userA")
# username.send_keys("lifei")
# pwd = driver.find_element_by_name("passwordA")
# pwd.send_keys("123456")
#根据标签里的class属性内容定位
# cla = driver.find_element_by_class_name("telAA")
# cla.send_keys("hello")
# 根据标签查找符合的第一个元素
# tag = driver.find_element_by_tag_name("input").send_keys("world")
# tag = driver.find_elements_by_tag_name("input")[0].send_keys("world")
'''
获取这一类标签集合，然后根据下标取第几个,下标从0开始
tag=driver.find_elements_by_tag_name("input")[0].send_keys("world")
'''
#link_text:获取文本内容必须是完整版
# driver.find_element_by_link_text("访问 新浪 网站").click()
#partial_link_text：获取文本内容可以是模糊查询一样
# driver.find_element_by_partial_link_text("访问").click()
'''xpath绝对路径定位，获取同级相同标签下元素必须从数字1开始'''
# driver.find_element_by_xpath("/html/body/form/div/fieldset/p[1]/input").send_keys("haha")
'''
1、xpath相对路径定位；相对路径以//开始，*匹配任何元素节点，@*匹配任何属性节点，//*选取文档中的所有元素
2、也可F12定位元素然后在HTML中右键copy——copy XPath(复制相对路径)
'''
#
# driver.find_element_by_xpath("//*[@id='userA']").send_keys("hehe")
'''
1、样式定位:必须以#开头，然后+（di/name属性内容）定位
2、样式也可定位标签：不用#开头，直接标签button.click()即可
3、也可F12定位元素然后在HTML中右键copy——copy selector(复制)
4、样式定位最快下来xpath在其他
'''
# driver.find_element_by_css_selector("#userA").send_keys("hello world")
# sleep(5)
# driver.find_element_by_css_selector("button").click()
'''清除'''
# driver.find_element_by_id("userA").send_keys("jsfs")
# driver.find_element_by_id("userA").clear()
'''定位对话框，获取对话框'''
#首先获取按钮点击
# driver.find_element_by_css_selector("#alerta").click()
#定位对话框
# alert = driver.switch_to.alert
'''
获取对话框内容，必须在关闭对话框之前获取，否则获取为空
'''
# text = alert.text
# print(text)
#确定；取消（dismiss()）
# alert.accept()

#获取文科框标签的大小
# size=driver.find_element_by_id("userA").size
# print(size)

#获取title
# ts = driver.title
# print(ts)
#获取当前路径
# curl = driver.current_url
# print(curl)
#获取a超链接标签的属性值
# hqtext = driver.find_element_by_id("fwA").get_attribute("href")
# print(hqtext)
'''
操作下拉框
'''
# options = driver.find_elements_by_tag_name("option")
'''两种方法'''
# for a in options:
#     if a.text == "A上海":
#         sleep(3)
#         a.click()
# for a in options:
#     if a.get_attribute("value") == "gz":
#         sleep(3)
#         a.click()
#         sleep(5)
'''下拉框第三种方法用css定位直接获取其中value属性'''
# sleep(3)
# options = driver.find_element_by_css_selector("[value='sh']").click()
'''
下拉框第四种方法用下拉框标签select中value属性定位，必须先导入select
from selenium.webdriver.support.select import Select
'''
# sleep(3)
#根据实例先根据下拉列表的id定位select标签
# select=Select(driver.find_element_by_css_selector("#selectA"))
#再根据下拉文本内容锁定
# select.select_by_visible_text("A广州")
'''窗口大小设置等'''
# driver.set_window_size(200,200)
#窗口最大化
# driver.maximize_window()
# sleep(3)
#后退
# driver.back()
# sleep(3)
#前进
# driver.forward()
# sleep(3)
#刷新
# driver.refresh()

'''滑动js,窗口滑动'''
# js1="window.scrollTo(0,1000)"
# js2='window.scrollTo(0,0)'
# driver.execute_script(js1)
# sleep(3)
# driver.execute_script(js2)
sleep(3)
'''定位iframe，在定位相应iframe下相应元素'''
# driver.switch_to.frame("myframe1")
# driver.find_element_by_id("userA").send_keys("jjj")

'''这里多个iframe时，进入一个iframe必须回到原来页面在从新进入另一个iframe'''
#回到最外边页面，因为上边访问了iframe注册A页面，在访问注册B页面就得返回
# driver.switch_to.default_content()
# driver.switch_to.frame("myframe2")
# driver.find_element_by_id("userB").send_keys("kkk")
'''
句柄：可以对某一个页面（iframe）去设定其固定的代号（代号是随机的不固定）
'''
#获取当前句柄
cur_handle = driver.current_window_handle
print ("句柄：",cur_handle)
sleep(3)
driver.find_element_by_css_selector("#ZCA").click()
sleep(3)
#获取页面所有handles句柄
handles=driver.window_handles
for a in handles:
    print(a)
    if a != cur_handle:
        driver.switch_to.window(a)
        sleep(3)
        driver.find_element_by_css_selector("#userA").send_keys("abcd")
sleep(3)
driver.quit()