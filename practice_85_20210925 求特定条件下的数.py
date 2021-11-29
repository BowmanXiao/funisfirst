'''
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

程序分析：999999 / 13 = 76923。
'''
# 方法一
n = int(input('请输入一个奇数：'))
i = 1
a = 10
while i:
    if (a - 1) % n == 0:
        print('最少%d个9除以该数的结果为整数。' % i)
        break
    i += 1
    a = 10 ** i

# 方法二
n = int(input('请输入一个奇数：'))
i = 1
a = 9
while i:
    if a % n == 0:
        print('最少%d个9除以该数的结果为整数。' % i)
        break
    i += 1
    a = a * 10 + 9
