'''
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

程序分析：无。
'''
with open('test1.txt', 'r') as p1:
    a = p1.read()
with open('test2.txt', 'r') as p2:
    b = p2.read()
c = list(a + b)
c.sort()
c = ''.join(c)
with open('test3.txt', 'w') as p3:
    p3.write(c)
re = open('test3.txt', 'r')
print(re.read())
re.close()
