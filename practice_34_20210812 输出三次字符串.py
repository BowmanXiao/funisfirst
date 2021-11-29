'''
题目：练习函数调用。

程序分析：使用函数，输出三次 RUNOOB 字符串。
'''

def prin():
    print('RUNOOB')
def triprin():
    for i in range(3):
        prin()
if __name__=='__main__':
    triprin()