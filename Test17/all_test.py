# coding=utf-8
import unittest
import HTMLTestRunner
import time
# 这里需要导入测试文件

# from Test17 import allcase_list

from Test17.test_case import start_baidu, start_youdao
listaa='D:\\AutoTest\\Test17\\test_case'
def creatsuitel():
    testunit=unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(listaa,pattern='start_*.py',top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
        print(testunit)
    return testunit

alltestnames = creatsuitel()
# testunit = unittest.TestSuite()
#获取数组方法
# alltestnames = allcase_list.caselist()

# 将测试用例加入到测试容器(套件)中
#循环读取数组中的用例
# for test in alltestnames:
#     testunit.addTest(unittest.makeSuite(test))
# 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)

# 定义个报告存放路径，支持相对路径
now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
print(now)
fp = open("result" + now + ".html", 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度搜索测试报告", description=u"用例执行情况")
# 运行测试用例
runner.run(alltestnames)
fp.close()
