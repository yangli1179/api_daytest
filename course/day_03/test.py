# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/14

E-mail:1179384105@qq.com

=================================


"""

# log日志
# import logging
# from common import logger
#
#
# logging.info("测试")

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j<=i:
#             print('{}*{}={}'.format(j, i, j*i), end='\t')
#     print('')


# 读写excel
# import os
# from common.constant import DATA_DIR
# from common import read_excel
#
# a = read_excel.ReadExcel(os.path.join(DATA_DIR, "students.xlsx"), "Sheet1")
# read = a.read_line_data()
# for i in read:
#     print(i.id, i.name, i.age)
# wrute = a.write_data(2, 4, "123")



# 发送邮件

# import os
# from common.config import conf
# from common.send_email import SendEmail
# from common.constant import REPORT_DIR
#
# title = conf.get("email", "mail_title")
# message = conf.get("email", "mail_message")
# file_path = os.path.join(REPORT_DIR, "report.html")
# email = SendEmail.send_qq_file_email(title=title, message=message, file_path=file_path)


# 九九乘法表

for i in range(1, 10):
    for j in range(1, 10):
        if j<=i:
            print("{}*{}={}".format(j, i, j*i), end="\t")
    print('')


