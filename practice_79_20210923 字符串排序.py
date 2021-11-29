'''
题目：字符串排序。

程序分析：无。
'''
if __name__ == '__main__':
    str1 = input('input a string:')
    str2 = input('input a string:')
    str3 = input('input a string:')
    if str1 > str2:
        str1, str2 = str2, str1
    if str1 > str3:
        str1, str3 = str3, str1
    if str2 > str3:
        str2, str3 = str3, str2
    print(str1, str2, str3)
