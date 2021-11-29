'''
题目：两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵。

程序分析：创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
'''

# 方法一 使用numpy数组生成矩阵并相加
import numpy as np

x = np.random.randint(1, 100, 9).reshape(3, 3)
y = np.random.randint(1, 100, 9).reshape(3, 3)
print('x = {}'.format(x))
print('y = {}'.format(y))
print('x + y = {}'.format(x + y))

# 方法二 使用列表推导式+randoms生成数组
import random

a = [[random.randint(1, 100) for i in range(3)] for j in range(3)]
b = [[random.randint(1, 100) for i in range(3)] for j in range(3)]
print(a)
print(b)
z = a[:]
for i in range(len(a)):
    for j in range(len(a[i])):
        z[i][j] = a[i][j] + b[i][j]
print(z)

# 方法三 用numpy的array()生成矩阵
x = np.array([[89, 7, 15], [17, 51, 31], [4, 81, 78]])
y = np.array([[69, 88, 26], [26, 57, 80], [8, 73, 39]])
print(x + y)
print()

# 方法四 用生成空矩阵
x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

z = []
for i in range(3):
    zz = list(map(lambda x, y: x + y, x[i], y[i]))
    z.append(zz)
print(z)
