'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
'''


# 方法一 一般函数
def get_sum1():
    a = input("输入单项值：")
    n = int(input("输入项数："))
    sum = 0
    print("s=", end='')
    for i in range(1, n + 1):
        value = int(a * i)
        sum += value
        if i == n:
            print(f'{value}', end='')
        else:
            print(f'{value}+', end='')
    print(f'={sum}')


get_sum1()

# 方法二 reduce()函数
from functools import reduce


def get_sum2():
    a = int(input("输入单项值："))
    n = int(input("输入项数："))
    item_list= []
    item = 0
    print("s=", end='')
    # for i in range(1, n + 1):
    #     val = a * int(str(1) * i)
    #     num.append(val)
    # Sum = sum(item_list)
    for i in range(0, n):
        item = item + a
        a = a * 10
        item_list.append(item)
    Sum = reduce(lambda x, y: x + y, item_list)
    l = '+'.join([str(x) for x in item_list])
    print('{}={}'.format(l, Sum))


get_sum2()
