#   Date: 2019/7/21 0021
#   Name: life
#  _*_ coding:UTF-8  _*_

from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
url="file:///E:/%E4%B9%90%E6%90%8Fpython%E8%87%AA%E5%8A%A8%E5%8C%96/python%E8%87%AA%E5%8A%A8%E5%8C%96%EF%BC%88%E5%BC%80%E8%AF%BE%E5%89%8D%E5%AE%89%E8%A3%85%EF%BC%89/%E5%A5%BD%E5%A8%81%E8%80%81%E5%B8%88%E4%B8%8A%E8%AF%BE%E4%BB%A3%E7%A0%81/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)

# username=driver.find_element_by_id("userA")
# username.send_keys("lifei")
# pwd=driver.find_element_by_name("passwordA")
# pwd.send_keys("123456")
#根据标签里的class属性内容定位
# cla=driver.find_element_by_class_name("telAA")
# cla.send_keys("hello")
# 根据标签查找符合的第一个元素
# tag=driver.find_element_by_tag_name("input").send_keys("world")
# tag=driver.find_elements_by_tag_name("input")[0].send_keys("world")
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
driver.find_element_by_xpath("//*[@id='userA']").send_keys("hehe")
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
'''获取对话框'''
#首先获取按钮点击
driver.find_element_by_css_selector("#alerta").click()
#定位对话框
alert=driver.switch_to.alert
'''
获取对话框内容，必须在关闭对话框之前获取，否则获取为空
'''
text=alert.text
print(text)
#确定；取消（dismiss()）
alert.accept()

#获取文科框标签的大小
size=driver.find_element_by_id("userA").size
print(size)

#获取title
ts=driver.title
print(ts)
#获取当前路径
curl=driver.current_url
print(curl)
#获取a超链接标签的属性值
hqtext=driver.find_element_by_id("fwA").get_attribute("href")
print(hqtext)
'''
操作下拉框
'''
options=driver.find_elements_by_tag_name("option")
'''两种方法'''
# for a in options:
#     if a.text == "A上海":
#         sleep(3)
#         a.click()
for a in options:
    if a.get_attribute("value") == "gz":
        sleep(3)
        a.click()
        sleep(5)

sleep(3)
driver.quit()