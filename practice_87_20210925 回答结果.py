'''
题目：回答结果（结构体变量传递）。

程序分析：无。
'''


class student():
    x = 0
    c = 0


def f(stu):
    stu.x = 20
    stu.c = 'a'


a = student()
a.x = 30
a.c = 'c'
f(a)
print(a.x, a.c)
