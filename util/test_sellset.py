# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/23

E-mail:1179384105@qq.com

=================================


"""

import unittest
from library.ddt import ddt, data
from common.read_excel import ReadExcel
from common import logger
import logging
from common.config import conf
import os
from common.constant import DATA_DIR
from common.http_request import HTTPRequest,HTTPRequest1
from common.execute_mysql import ExecuteMsql
from common.tools import get_token, rand_name


# 从配置文件获取数据
file_name = conf.get("excel", "file_name")



@ddt
class SellerSettingTestCase(unittest.TestCase):
    # 拼接完整的excel路径，然后读取excel数据
    wb = ReadExcel(os.path.join(DATA_DIR, "test_cases.xlsx"), "seller-setting")
    cases = wb.read_line_data()

    @classmethod
    def setUpClass(cls):
        logging.info("==================== 准备开始执行销售方发票信息接口测试 ====================")
        cls.request = HTTPRequest()
        cls.request1 = HTTPRequest1()
        cls.db = ExecuteMsql()

    @classmethod
    def tearDownClass(cls):
        logging.info("==================== 销售方发票信息测试执行完毕 ====================")
        cls.request.close()


    @data(*cases)
    def test_sellset(self, case):
        # 拼接url
        url = conf.get("env", "fscurl") + case.url
        self.row = case.case_id + 1

        # 获取token
        token = get_token(phone=eval(case.token_data)["phone"], pwd=eval(case.token_data)["code"])

        # headers = {"fsp_token": token}
        headers = {"Authorization": case.request_header.replace("#token", token), "Content-Type": "application/json;charset=UTF-8",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                   "Referer": "https://fsc-test.manshang.com/app/invoice/ApplyDetail/Apply",
                   "Origin": "https://fsc-test.manshang.com",
                   "Accept-Encoding": "gzip, deflate, br"}


        # 发送请求，请求参数为字典类型
        response = self.request.request(method=case.method, url=url, data=eval(case.request_data), headers=headers)

        # 以下打印内容会显示在html报告中
        print()
        print("请求地址--> {}".format(url))
        print("请求数据--> {}".format(case.request_data))
        print("期望结果--> {}".format(case.expected_data))
        print("服务器响应数据--> {}".format(response.json()))

        res = response.json()

        try:
            self.assertEqual(res, eval(case.expected_data))
        except AssertionError as e:
            result = "FAIL"
            logging.exception(e)
            raise e

        else:
            result = "PASS"
            logging.info("预期结果是：{}，实际结果是：{}，测试通过".format(case.expected_data, res))

        finally:
            self.wb.write_data(self.row, 11, str(res))
            self.wb.write_data(self.row, 12, result)
