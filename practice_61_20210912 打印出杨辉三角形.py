'''
题目：打印出杨辉三角形（要求打印出10行如下图）。　　

程序分析：无。
'''
# 1.列表推导式
# 2.numpy数组
# 3.for循环打印
# 4.print格式输出
a = []


def yanghui(n):
    for i in range(n):
        a.append([])
        for j in range(i + 1):
            a[i].append(0)
    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in a:
        for j in i:
            print(j, end='\t')
        print()


yanghui(11)

