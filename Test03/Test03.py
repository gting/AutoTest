# Coding=utf-8
from selenium import webdriver
import os
import time

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

# 选择页面上所有的 tag name 为 input 的元素
# inputs = driver.find_elements_by_tag_name('input')
#
# # 然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()

# 选择所有的type为checkbook的元素并单击勾选
checkboxes=driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()

# 打印当前页面上type为checkbook的个数
print(len(driver.find_elements_by_css_selector('input[type=checkbox]')))

# 把页面最后一个checkbox的勾去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(3)

driver.quit()
