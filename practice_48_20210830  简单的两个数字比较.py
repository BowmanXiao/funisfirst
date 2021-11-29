'''
题目：数字比较。

程序分析：无
'''


# 方法一  if分支语句进行判断
def comp1(num1, num2):
    if num1 > num2:
        print('%d比%d大' % (num1, num2))
    elif num1 == num2:
        print('%d和%d一样大' % (num1, num2))
    else:
        print('%d比%d小' % (num1, num2))


if __name__ == '__main__':
    num1 = int(input('请输入第一个数：'))
    num2 = int(input('请输入第二个数：'))
    comp1(num1, num2)


# max()和min()内嵌函数
def comp2(num1, num2):
    if num1 == num2:
        print('%d和%d一样大' % (num1, num2))
    else:
        maxN = max(num1, num2)
        minN = min(num1, num2)
        print('%d比%d大' % (maxN, minN))
if __name__ == '__main__':
    num1 = int(input('请输入第一个数：'))
    num2 = int(input('请输入第二个数：'))
    comp2(num1, num2)