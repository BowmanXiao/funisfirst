'''
题目：模仿静态变量的用法。

程序分析：无。
'''


def varfunc():
    var = 0
    print('var=%d' % var)
    var += 1


if __name__ == "__main__":
    for i in range(3):
        varfunc()


# 类的属性
class Static:
    Staticvar = 5

    def varfunc(self):
        self.Staticvar += 1
        print(self.Staticvar)


print(Static.Staticvar)
a = Static()
for i in range(3):
    a.varfunc()  # 实例对象的静态变量改变
    print(Static.Staticvar)  # 实例对象的静态变量改变不影响类的静态变量
    Static.Staticvar += 1  # 类的静态变量改变
