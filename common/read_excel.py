# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/15

E-mail:1179384105@qq.com

=================================


"""


import openpyxl


class Case(object):

    # 用这个类来处理打包后的数据，将每对打包的第一个值设置成属性名，第二个值设置成属性名对应的值
    # attrs为一个zip对象，有几列数据就有几个zip对象
    def __init__(self, attrs):
        for item in attrs:
            # 将属性名和属性值组装起来
            setattr(self, item[0], item[1])


class ReadExcel(object):
    def __init__(self, file_path, sheet_name):
        self.file_name = file_path
        self.sheet_name = sheet_name

    def open(self):
        # 传入指定文件名，打开工作簿
        self.wb = openpyxl.load_workbook(self.file_name)
        # 选取表单
        self.sheet = self.wb[self.sheet_name]

    def close(self):
        self.wb.close()

    # 按行读取数据
    def read_line_data(self):
        # 打开工作簿
        self.open()
        # 按行读取数据并转换成列表
        rows_data = list(self.sheet.rows)

        # 定义一个空列表，存储表单的表头信息
        titles = []
        for title in rows_data[0]:
            # 对title是否为空进行过滤，这是容错机制
            if title.value:
                titles.append(title.value)

        # 定义一个空列表，用来存储所有的数据
        cases = []
        # 从第二行开始就是测试用例数据
        for case in rows_data[1:]:
            # 定义一个空列表，用来临时存放每行的用例数据
            data = []
            for cell in case:
                data.append(cell.value)

            # 将title与测试用例数据组合，形成每行测试数据，一行行读取，无需加list
            case_data = zip(titles, data)
            # 创建一个Case类的对象，用来保存用例数据
            case_obj = Case(case_data)
            cases.append(case_obj)

        # 关闭工作簿
        self.close()
        return cases

    def write_data(self, row, column, value):
        self.open()
        # 指定位置写入数据
        self.sheet.cell(row=row, column=column, value=value)
        # 保存数据
        self.wb.save(self.file_name)
        # 关闭工作簿
        self.close()


if __name__ == '__main__':

    import os
    from common.constant import DATA_DIR
    readexcel = ReadExcel(os.path.join(DATA_DIR, "students.xlsx"), "Sheet1")
    excel = readexcel.read_line_data()
    print(excel)
    for a in excel:
       print(a.id, a.name, a.age)
    res = readexcel.write_data(row=2, column=4, value="java")









