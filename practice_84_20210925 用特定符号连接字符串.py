'''
题目：连接字符串。

程序分析：无。
'''
delimeter = ', '
mylist = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
str1 = delimeter.join(mylist)
print(str1)
print(str1.split(', '))

lis = []
for i in mylist:
    lis.append(i[0])
print(lis)
print(''.join(lis))
# for a in mylist:
#     print(a[0], end='')
