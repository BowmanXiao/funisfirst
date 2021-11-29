'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。

程序分析：无
'''

# 方法一 while循环+if判断语句, continue
while True:
    x = int(input("请输入一个数字，使其平方大于等于50："))
    if x ** 2 < 50:
        print("请重新输入！")
        continue
    else:
        print(x ** 2)

# 方法二 while循环+if判断语句, break
while True:
    x = int(input("请输入一个数字，使其平方大于等于50："))
    if x ** 2 < 50:
        break
    else:
        print(x ** 2)