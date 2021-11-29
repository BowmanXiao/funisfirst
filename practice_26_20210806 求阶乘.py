'''
题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!
'''

# 递归法，千万不能漏了n==1时的分支语句
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
