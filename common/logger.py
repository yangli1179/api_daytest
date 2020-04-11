# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/14

E-mail:1179384105@qq.com

=================================


"""


import logging
from logging.handlers import RotatingFileHandler
import time
from common.constant import LOGS_DIR
from common.config import conf

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
date_fmt = '%a, %d %b %Y %H:%M:%S'

# 输出到控制台
handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

log_name = conf.get("logs", "log_name")
log_path = LOGS_DIR + '{}_{}.log'.format(log_name, curTime)

# 输出文件
handler_2 = RotatingFileHandler(log_path, backupCount=20, encoding='utf-8')

# 设置日志输出的内容形式，输出渠道
logging.basicConfig(format=fmt, datefmt=date_fmt, level=logging.INFO, handlers=[handler_1, handler_2])


if __name__ == '__main__':
    logging.info("aaa")
