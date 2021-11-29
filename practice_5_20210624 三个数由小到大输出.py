'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
'''
# 方法一：if判断
# !/usr/bin/python
# -*- coding:utf-8 -*-
x = input("请输入x:")
y = input("请输入y:")
z = input("请输入z:")
if x > y:
    a = x
    x = y
    y = a
if x > z:
    b = x
    x = z
    z = b
if y > z:
    c = y
    y = z
    z = c
print(x, y, z)

# 方法二：数值对调
# !/usr/bin/python
# -*- coding:utf-8 -*-
x = input("请输入x:")
y = input("请输入y:")
z = input("请输入z:")
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)

#方法三：列表sort1
#!/usr/bin/python
#-*- coding:utf-8 -*-
num=[]
for i in range(5):
    num.append(int(input('请输入整数：')))
num.sort()
print(num)

#方法四：冒泡排序-while嵌套
#!/usr/bin/python
#-*- encoding:utf-8 -*-
num = []
for i in range(5):
    item = input("请输入整数:")
    while item =='':
        item = int(input("请重新输入整数:"))
    num.append(int(item))
for item in num:
    print(item, end=' ')
m = len(num)
while m != 1:
    for i in range(m - 1):
        if num[i] > num[i + 1]:
            tmp = num[i]
            num[i] = num[1 + 1]
            num[i + 1] = tmp
    m -= 1
print(num)

# 方法五：冒泡排序-for嵌套
# !/usr/bin/python
# -*- encoding:utf-8 -*-
num = []
for i in range(5):
    num.append(int(input("请输入整数:")))
for item in num:
    print(item, end=' ')
m = len(num)
for i in range(0, m):
    for j in range(i, m):
        if num[i] > num[j]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp
print(num)
