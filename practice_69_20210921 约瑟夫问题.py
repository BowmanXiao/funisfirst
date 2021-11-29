'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

程序分析：无。
'''

# 方法一
n = int(input('请输入总人数：'))
lis = [i + 1 for i in range(n)]
print(lis)
i = 0
k = 0
m = 0
print('i\t', 'm\t', 'k\t')
while m < n - 1:
    if lis[i] != 0:
        k += 1
    if k == 3:
        lis[i] = 0
        m += 1
        k = 0
    i += 1
    if i == n:
        i = 0
    print('{}\t{}\t{}\t'.format(i, m, k))
print(lis)
i = 0
for i in range(n):
    if lis[i] != 0:
        print(lis[i])

# 方法二
n2 = 34
lis2 = [i + 1 for i in range(n)]
i = 1
while len(lis2):
    if i % 3 != 0:
        lis2.insert(len(lis2), lis2.pop(0))
    else:
        lis2.pop(0)
    i += 1
for i in lis:
    if i != 0:
        print(i)
