'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
'''
# -*- coding:utf-8 -*-
# 方法一
for num in range(100, 1000):
    i = num // 100
    j = num // 10 % 10
    k = num % 10
    if i ** 3 + j ** 3 + k ** 3 == num:
        print(num)
print('\n')

# 方法二
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            num = i * 100 + j * 10 + k
           #num = int(str(i)+str(j)+str(k))
            if num == i ** 3 + j ** 3 + k ** 3:
                print(num)
print('\n')

# 方法三
for i in range(100, 1000):
    num = str(i)
    if int(num[0]) ** 3 + int(num[1]) ** 3 + int(num[2]) ** 3 == i:
        print(i)
print('\n')

# 方法四
l = []
for num in range(100, 1000):
    i = num // 100
    j = (num - i * 100) // 10
    k = num % 10
    if pow(i, 3) + pow(j, 3) + pow(k, 3) == num:
        l.append(num)
print(l)
print('\n')

# 方法五
print([i for i in range(100, 1000) if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i])
