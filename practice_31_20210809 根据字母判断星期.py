'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

程序源代码：
'''
# Monday Tuesday Wednesday Thursday Friday Saturday Sunday
x = input("请输入第一个字母（区分大小写）：")
while x not in ['M', 'T', 'W', 'F', 'S']:
    x = input("请重新输入第一个字母：")
else:
    if x == 'M':
        print('Monday')
    elif x == 'W':
        print('Wednesday')
    elif x == 'F':
        print('Friday')
    elif x == 'T':
        y = input("请输入第二个字母（区分大小写）：")
        while y not in ['u', 'h']:
            y = input("请重新输入第二个字母：")
        else:
            if y == 'u':
                print('Tuesday')
            else:
                print('Thursday')
    else:
        y = input("请输入第二个字母（区分大小写）：")
        while y not in ['a', 'u']:
            y = input("请重新输入第二个字母：")
        else:
            if y == 'a':
                print('Saturday')
            else:
                print('Sunday')
