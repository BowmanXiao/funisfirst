'''
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

程序分析：无。
'''
# 方法一 循环求解
def fun(n):
    a = 0
    s = 0
    if n % 2 == 0:
        a = 2
    else:
        a = 1
    while a <= n:
        s += 1 / a
        a += 2
    print(s)
fun(9)

# 方法二 递归函数
def fun2(n):
    if n % 2 == 0:
        if n==2:
            return 1/2
        else:
            return fun2(n-2)+1/n
    else:
        if n==1:
            return 1
        else:
            return fun2(n-2)+1/n
print(fun2(9))
