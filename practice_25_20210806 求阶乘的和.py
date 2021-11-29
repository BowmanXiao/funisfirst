'''
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。
'''

# 方法一 for循环求解

sum = 0
item = 1
for i in range(1, 21):
    item *= i
    sum += item
print(sum)


# 方法二 两个递归函数嵌套

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


def get_sum(n):
    if n == 1:
        return 1
    else:
        return get_sum(n - 1) + fac(n)


print(get_sum(20))
