'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''


# 方法一 直接判断
def get_num0():
    tempStr = input("请输入一段文本：")
    letter = 0
    space = 0
    digit = 0
    others = 0
    for i in tempStr:
        if i.isalpha():
            letter += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            others += 1
    print('''
    中英文数：{}
    空格数：{}
    数字数：{}
    其他数：{}
    '''.format(letter, space, digit, others))


get_num0()


# 方法二 字典
def get_num1():
    tempStr = input("请输入一段文本：")
    num_dic = {"letter": 0, "space": 0, "digit": 0, "others": 0}
    for i in tempStr:
        if i > 'a' and i < 'z' or i > 'A' and i < 'Z':
            num_dic["letter"] += 1
        elif i==' ':
            num_dic["space"] += 1
        elif i in '0123456789':
            num_dic["digit"] += 1
        else:
            num_dic["others"] += 1
    print('''
    中英文数：{}
    空格数：{}
    数字数：{}
    其他数：{}
    '''.format(num_dic["letter"], num_dic["space"], num_dic["digit"], num_dic["others"]))
get_num1()
