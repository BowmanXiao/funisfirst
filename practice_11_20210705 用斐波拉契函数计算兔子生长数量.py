'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
'''


# !/usr/bin/python
# -*- coding:utf-8 -*-
# 方法一 面向过程1
import math

mon = int(input("请输入月份："))
while not 1 <= mon <= 50:
    print("输入有误！")
    mon = int(input("请重新输入月份："))
f1 = 1
f2 = 1
if mon == 1 or mon == 2:
    print(f'第{mon}月后的兔子总对数为1。')
else:
    for i in range(1, mon - 1):
        f1 += f2
        f2 += f1
        if i == math.ceil(mon / 2) - 1:
            if mon % 2 == 1:
                print(f'第{mon}月后的兔子总对数为{f1}。')
            elif mon % 2 == 0:
                print(f'第{mon}月后的兔子总对数为{f2}。')
            break

# 方法二 面向过程2
mon = int(input("请输入月份："))
while not 1 <= mon <= 50:
    print("输入有误！")
    mon = int(input("请重新输入月份："))
f1 = 1
f2 = 1
if mon == 1 or mon == 2:
    print(f'第{mon}月后的兔子总对数为1。')
else:
    for i in range(mon - 1):
        f1, f2 = f2, f1 + f2
    print(f'第{mon}月后的兔子总对数为{f1}。')

# 方法三 面向过程
def get_RabNum():
    mon = int(input("请输入月份："))
    while not 1 <= mon <= 50:
        print("输入有误！")
        mon = int(input("请重新输入月份："))
    f1, f2 = 1, 1
    if mon == 1 or mon == 2:
        print(f'第{mon}月后的兔子总对数为1。')
    else:
        for i in range(mon - 1):
            f1, f2 = f2, f1 + f2
        print(f'第{mon}月后的兔子总对数为{f1}。')

num = rab_mon(8)
num.get_RabNum()

# 方法四 面向对象
class rab_mon(object):
    def __init__(self):
        self.mon = int(input("请输入月份："))
        while not 1 <= self.mon <= 50:
            print("输入有误！")
            self.mon = int(input("请重新输入月份："))

    def get_RabNum(self):
        f1, f2 = 1, 1
        if self.mon == 1 or self.mon == 2:
            print(f'第{self.mon}月后的兔子总对数为1。')
        else:
            for i in range(self.mon - 1):
                f1, f2 = f2, f1 + f2
            print(f'第{self.mon}月后的兔子总对数为{f1}。')

num=rab_mon()
num.get_RabNum()
