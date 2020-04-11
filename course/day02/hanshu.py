# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/13

E-mail:1179384105@qq.com

=================================


"""


from common.constant import CONF_DIR
from common.config import conf

host = conf.get("mysql", "host")
print(host)


def test(num, num1, num2=10):
    res = num + 1
    res1 = num1 + 10
    return res, res1, num2


def demo(num, *num1, **num2):
    print(num)
    print(num1)
    print(num2)


def demo1(num1,num2,num3):
    print(num1)
    print(num2)
    print(num3)

if __name__ == '__main__':
    pass
    # print(CONF_DIR)
    # a, b, c = test(2, num1=3, num2=20)
    # print(a)
    # print(b)n
    # print(c)
    # d = demo(1, 2, 3, **{"asd": 111})
    # print(d)
    # b = (1, 2, 3)
    # demo1(*b)
    # # a = (1, 2, 3)
    # # demo1(a[0], a[1], a[2])

    # eval函数
    # a = '{"username": "tom"}'
    # b = eval(a)
    # c = b["username"]
    # print(c)

    # a = '[1, 2, 3]'
    # a = eval(a)
    # print(type(a))
