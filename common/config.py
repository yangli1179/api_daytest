# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/13

E-mail:1179384105@qq.com

=================================


"""


import configparser
import os
from common.constant import CONF_DIR


class ReadConfig(configparser.ConfigParser):
    def __init__(self):
        # 调用父类的init方法
        super().__init__()
        # 读取配置文件
        self.read(os.path.join(CONF_DIR, "env.ini"), encoding="utf8")
        # 读取后可直接使用self.get获取配置文件中的值
        version = self.get("env", "version")
        if version == 'test':
            self.read(os.path.join(CONF_DIR, "config_test.ini"), encoding="utf8")
        elif version == 'produce':
            self.read(os.path.join(CONF_DIR, "config_produce.ini"), encoding="utf8")


conf = ReadConfig()

if __name__ == '__main__':
    host = conf.get("mysql", "host")
    print(host)
