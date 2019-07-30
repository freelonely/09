#   Date: 2019/7/30 0030
#   Name: life
#  _*_ coding:UTF-8  _*_


from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
url="https://mail.163.com/"
# 隐式等待
driver.implicitly_wait(10)
driver.get(url)
driver.find_element_by_id("switchAccountLogin").click()
driver.switch_to.frame(0)
driver.find_element_by_css_selector(".u-input.box input").send_keys("yeml8263")
driver.find_element_by_name("password").send_keys("a123456789")
sleep(3)
driver.find_element_by_id("dologin").click()
sleep(2)
assert "yeml8263@163.com" in driver.page_source
driver.find_element_by_xpath("//*[@id='_mail_component_24_24']/span[2]").click()
sleep(3)
driver.find_element_by_css_selector(".nui-ipt .nui-editableAddr-edit input").send_keys("18691737545")
driver.find_element_by_css_selector(".bz0 .nui-ipt > input").send_keys(u"关于学习")
# driver.find_element_by_css_selector("//*[@class='O0']").send_keys(r"C:\Users\Administrator\Desktop\123.jpg")
driver.switch_to_frame(driver.find_element_by_css_selector(".APP-editor-iframe"))
driver.find_element_by_tag_name("body").send_keys("好好学习，天天向上！！！")

driver.switch_to.default_content()
tes=driver.find_elements_by_xpath("//div[@class='nui-toolbar-item']/div/span[2]")
for a in tes:
    if a.text == "发送":
        a.click()
        break
sleep(5)
driver.quit()