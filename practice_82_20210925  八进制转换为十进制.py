'''
题目：八进制转换为十进制

程序分析：无。
'''


def f8t10():
    num = input('请输入一个八进制数：')
    Dnum = 0
    for i in range(len(num)):
        Dnum += 8 ** i*int(num[len(num)-1-i])
    print(f'八进制数:{num}\n转化为十进制数为：{Dnum}')


f8t10()
