'''
题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
'''
# 方法一 for循环
# !/usr/bin/python
# -*- coding:utf-8 -*-
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j}',end=' ')
    print()

# 方法二 while循环
i=1
while i<=9:
    j=1
    while j<=i:
        print(f'{j}*{i}={i*j}', end=' ')
        j+=1
    print()
    i+=1

# 方法三 break关键字
# !/usr/bin/python
# -*- coding:utf-8 -*-
for i in range(1,10):
    for j in range(1,10):
        print('{}*{}={}'.format(j,i,i*j),end=' ')
        if i==j:
            print()
            break

# 方法四 %输出格式
# !/usr/bin/python
# -*- coding:utf-8 -*-
for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%d'%(j,i,i*j),end=' ')
        if i==j:
            print()
            break
