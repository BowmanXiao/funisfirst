'''
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。
'''

# 方法一 reverse()函数
lis = [1, 3, 5, 2, 6, 9, 8, 7]
lis.reverse()
print(lis)

# 方法二 切片
lis = [1, 3, 5, 2, 6, 9, 8, 7]
a = lis[::-1]
print(a)

# 方法三 pop()函数
lis = [1, 3, 5, 2, 6, 9, 8, 7]
d = []
for i in range(len(lis)):
    d.append(lis.pop())
print(d)

# 方法四  首尾交换数值
lis = [1, 3, 5, 2, 6, 9, 8, 7]
for i in range(len(lis) // 2):
    lis[i], lis[len(lis) - 1 - i] = lis[len(lis) - 1 - i], lis[i]
print(lis)

# 方法五  逆序取值
lis = [1, 3, 5, 2, 6, 9, 8, 7]
d = []
for i in range(len(lis)):
    d.append(lis[len(lis) - 1 - i])
# for i in range(-1, -len(lis)-1, -1):
#     d.append(lis[i])
print(d)
