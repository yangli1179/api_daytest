# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/12

E-mail:1179384105@qq.com

=================================


"""

import random
from common.http_request import HTTPRequest


def random_ip():
    ip = "{}.{}.{}.{}".format(random.randint(0, 255), random.randint(0, 255),
                              random.randint(0, 255), random.randint(0, 255))
    return ip


def get_token(phone, pwd, nationCode=86):
    request = HTTPRequest()
    method = "post"
    url = "https://api.b.mydaydream.com/passport/passportv2/mobilePhoneLogin"
    data = {"code": pwd,"mobilePhone": phone}
    response = request.request(method=method, url=url, json=data)
    res = response.json()
    token = res['data']['authToken']
    print("token是：{}".format(token))
    return token


# 获取随机的用户名，由6位包括数字，大写，小写字母组成
def rand_name():
    name = ""
    for i in range(6):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))  # ASCII表示数字
        letter = chr(random.randint(97, 122))   # 取小写字母
        Letter = chr(random.randint(65, 90))    # 取大写字母
        s = str(random.choice([num, letter, Letter]))
        name += s
    return name

# 获取分页总数
def get_pagenum(total, pagesize):
    num = (total + pagesize - 1)//pagesize
    return num


# 获得关注用户的uid
def get_followuid():
    request = HTTPRequest()
    method = "get"
    url = "https://api.b.mydaydream.com/dreamAppV3/user/getFollowList"
    params = {"page": 1, "size": "10"}
    token = get_token(phone="15733100728", pwd="123456")
    headers = {'x-access-token': token}
    response0 = request.request(method=method, url=url, params=params, headers=headers)
    res1 = response0.json()

    # 获取关注用户总数量
    count = res1['data']['count']

    # 获取总页数
    page = get_pagenum(count, 10)
    print(page)
    uid = []
    for i in range(0, count):
        res = res1['data']['data'][i]['uid']
        uid.append(res)
    return uid, count

# 获取个人主页是否关注
def get_isfollow():
    request = HTTPRequest()
    method = "get"
    url = "https://api.b.mydaydream.com/dreamAppV3/User/homepage?viewUid=18799&viewBid="
    token = get_token(phone="15733100728", pwd="123456")
    headers = {'x-access-token': token}
    response = request.request(method=method, url=url, headers=headers)
    res = response.json()
    isFollow = res['data']['isFollow']
    return isFollow





if __name__ == '__main__':
    # token = get_token("15733100728", "123456")
    # print(token)
    # name = rand_name()
    # print(name)
    # a = get_followuid()
    # print(a)
    b = get_isfollow()
    print(b)




