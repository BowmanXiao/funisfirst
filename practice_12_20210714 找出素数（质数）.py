'''
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
'''
# !/usr/bin/python
# -*- coding:utf-8 -*-
# 方法一
from math import *

l = list(range(101, 201))
for i in range(101, 201):
    for j in range(2, int(sqrt(i) + 1)):
        if i % j == 0:
            l.remove(i)
            break
print(f'101-201之间有{len(l)}个素数，分别为：{l}')

# 方法二
l = []
for i in range(101, 201):
    for j in range(2, int(sqrt(i) + 1)):
        if i % j == 0:
            break
    else:  # 注意else语句的缩进，见下面的程序
        l.append(i)
print('101-201之间有{}个素数，且分别是：{}'.format(len(l), l))

# else和for搭配探究
for i in range(10):
    if i == 8:
        print('Found it %s' % i)
        break
else:
    print('Not found!')


# 方法三 自定义函数
def get_num(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            break
    else:
        return num


l = []
for num in range(101, 201):
    if get_num(num):
        l.append(get_num(num))
print(len(l), l)
