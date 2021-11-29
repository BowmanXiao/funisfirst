'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

程序分析：无。
'''
n = 1
while n < 8:
    num = int(input('请输入一个整数：'))
    if num in range(1, 51):
        print(num * '*')
    else:
        print('请重新输入1-50的整数值！')
    n += 1
