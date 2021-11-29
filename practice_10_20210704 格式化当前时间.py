'''
题目：暂停一秒输出，并格式化当前时间。

程序分析：无。
'''
# !/usr/bin/python
# -*- coding:utf-8 -*-
import time, datetime
print(datetime.datetime.now())
time.sleep(1)
print(time.time())
time.sleep(2)
while True:
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    time.sleep(1)

