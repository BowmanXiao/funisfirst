'''
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
'''
# !/usr/bin/python
# -*- coding:utf-8 -*-
# 方法一
import time

l = [1, 2, 3, 4]
for i in l:
    print(i)
    time.sleep(1)

# 方法二
import time

MyD = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
for key, value in MyD.items():
    print(key, value)
    time.sleep(1)
