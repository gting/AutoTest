# Coding = utf-8
from selenium import webdriver

import time

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

# 获得Cookie信息
cookies=driver.get_cookies()

# 打印获得的Cookie信息
print(cookies)

# 向Cookies中的name和value添加会话信息
driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})

# 遍历cookies中的name和value信息打印
for cookie in driver.get_cookies():
    print("%s->%s"%(cookie['name'],cookie['value']))

# 删除特定的cookie
driver.delete_cookie("CookieName")

# 删除所有的cookie
driver.delete_all_cookies()

time.sleep(2)

driver.quit()