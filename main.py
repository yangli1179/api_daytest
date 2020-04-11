# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/17

E-mail:1179384105@qq.com

=================================


"""

import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.config import conf
from common.constant import CASES_DIR, REPORT_DIR
from common.send_email import SendEmail
import os
import time


_title = conf.get('report', 'title')
_description = conf.get('report', 'description')
_tester = conf.get('report', 'tester')
report_name = conf.get('report', 'report_name')
report_name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + "_" + report_name
mail_title = conf.get('email', 'mail_title')
mail_message = conf.get('email', 'mail_message')
file_path = os.path.join(REPORT_DIR, report_name)

suite = unittest.TestSuite()  # 创建测试集合
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASES_DIR))

with open(file_path, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title=_title,
        description=_description,
        tester=_tester
    )
    runner.run(suite)


# 发送qq邮件
# file_path = SendEmail.new_file(REPORT_DIR)
# title = conf.get("email", "mail_title")
# message = conf.get("email", "mail_message")
# SendEmail.send_qq_file_email(title=title, message=message, file_path=file_path)

