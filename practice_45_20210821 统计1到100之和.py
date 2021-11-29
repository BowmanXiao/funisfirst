'''
题目：统计 1 到 100 之和。

程序分析：无
'''

# 方法一 for循环
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 方法二 while循环
sum = 0
n = 0
while n < 101:
    sum += n
    n += 1
print(sum)


# 方法三 递归函数
def get_sum(n):
    if n == 1:
        return 1
    else:
        return get_sum(n - 1) + n


print(get_sum(100))

# 方法四 sum()函数
del sum  # 删去前面定义的整形变量sum，以免与sum()冲突
print(sum(range(1,101)))
