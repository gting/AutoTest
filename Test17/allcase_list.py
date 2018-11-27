# coding=utf-8
# 把 test_case 目录添加到 path 下，这里用的相对路径
import sys

from Test17.test_case import start_youdao, start_baidu

sys.path.append("\\test_case")
from Test17.test_case import *


# 用例文件列表
def caselist():
    alltestnames = [
        start_baidu.Baidu,
        start_youdao.Youdao,

    ]
    print("success read case list!!")
    return alltestnames
