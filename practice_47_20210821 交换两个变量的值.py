'''
题目：两个变量值互换。

程序分析：无
'''


def shuru():
    a = int(input("请输入a的值："))
    b = int(input("请输入b的值："))
    print('a = %d, b = %d' % (a, b))
    return (a, b)


def exchange1(a, b):
    a, b = b, a
    print("第一种交换后，a = %d, b = %d" % (a, b))


def exchange2(a, b):
    t = a
    a = b
    b = t
    print("第二种交换后，a = %d, b = %d" % (a, b))


def exchange3(a, b):
    a = a + b
    b = a - b
    a = a - b
    print("第三种交换后，a = %d, b = %d" % (a, b))


if __name__ == '__main__':
    a, b = shuru()
    exchange1(a, b)
    exchange2(a, b)
    exchange3(int(a), int(b))
