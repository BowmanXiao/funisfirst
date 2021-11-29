'''
题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数

程序分析：无。
'''
# 方法一  列表切片
import random


def nList(n):   # 生成n个整数的列表
    a = [random.randint(1, 100) for i in range(n)]
    print(a)
    return a


def mAlter(a, n, m):   # a为生成的列表，n为列表长度，m为后移m个位置
    print(a[n - m:n] + a[0:n - m])


mAlter(nList(10), 10, 3)

# 方法二 pop()函数
import random


def nList2(n):
    a = [random.randint(1, 100) for i in range(n)]
    print(a)
    return a


def mAlter2(a, m):
    for i in range(m):
        p = a.pop()    # 删去列表最后一个元素，并存到变量p中
        a.insert(0, p)   # 将变量p存储的数值插入到列表首位
    print(a)
mAlter2(nList2(10), 3)