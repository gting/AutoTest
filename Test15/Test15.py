# coding=utf-8
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
# 捕捉百度输入框异常
try:
    browser.find_element_by_id("kwsss").send_keys("selenium")
    browser.find_element_by_id("su").click()
except:
    browser.get_screenshot_as_file("D:/error_png.png")
browser.quit()
