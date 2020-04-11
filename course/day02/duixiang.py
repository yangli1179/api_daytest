# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/13

E-mail:1179384105@qq.com

=================================


"""

# 优先级：实例方法、类方法、静态方法
# 同级可以调用自己及下级，下级不能调用上级，调用时需要写上self.xx  cls.xx
# 定义属性和变量时一般只在初始化时定义

class TestCase(object):
    # 定义类属性
    age = 18

    # 定义初始化方法，只要该类被调用就会执行该方法
    def __init__(self):
        self.name = "tom"  #实例属性
        print("这是初始化方法")

    def test1(self):
        print("111")
        print(self.name)
        self.test3()
        print(self.age)

    def test2(self):
        print("222")
        self.test1()

    # 类方法，不需要实例化，直接调用
    @classmethod
    def test3(cls):
        print("333")
        cls.test4()
        print(cls.age)


    # 静态方法，不需要实例化，直接调用
    @staticmethod
    def test4():
        print("444")


if __name__ == '__main__':

    case = TestCase()
    case.test1()
    case.test2()
    name = case.name
    print(name)
    TestCase.test3()
    TestCase.test4()
    # a = TestCase().test(18)
