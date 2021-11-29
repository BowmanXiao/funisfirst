'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

程序分析：无。
'''
# 方法一  单个输入，保存在列表中
print("请输入5个英文字符（单个输入）：")
stri = []
while 1:
    stri.append(input())
    if len(stri) == 5:
        break
print(stri[::-1])  # 分片倒序输出

# 方法二  字符串转列表
stri = input("请输入5个英文字符：")
print(stri[::-1])   # 分片倒序输出
print(list(reversed(stri)))  # reversed()函数，注意函数返回的是一个迭代器，需要用list()转换成列表
print(sorted(stri, reverse=True))  # sorted()函数