'''
题目：求一个3*3矩阵主对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''

# 方法一 手动生成二阶空矩阵
a = [[], [], []]
Sum = 0.0
for i in range(3):
    for j in range(3):
        a[i].append(float(input("请输入矩阵的值：")))
for i in range(3):
    Sum += a[i][i]
print(Sum)

# 方法二 手动输入矩阵并求值
a = []
Sum = 0.0
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(float(input("请输入矩阵的值：")))
for i in range(3):
    Sum += a[i][i]
print(Sum)

# 方法三 调用numpy数组模块
import numpy as np

a = np.random.randint(1, 100, 9).reshape(3, 3)
print(a)
(m, n) = np.shape(a)
print((m, n))
sum = 0
for i in range(m):
    for j in range(n):
        if i == j:
            sum += a[i][j]
print(sum)
