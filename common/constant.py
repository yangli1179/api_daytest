# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/13

E-mail:1179384105@qq.com

=================================


"""


import os


# 获取项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

CONF_DIR = os.path.join(BASE_DIR, "conf")

LOGS_DIR = os.path.join(BASE_DIR, "logs")

REPORT_DIR = os.path.join(BASE_DIR, "report")

CASES_DIR = os.path.join(BASE_DIR, "test_cases")


if __name__ == '__main__':
    print(BASE_DIR)
    print(DATA_DIR)
