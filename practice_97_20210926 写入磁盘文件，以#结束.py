'''
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

程序分析：无。
'''
# 方法一
str0 = ''
while 1:
    s = input('请逐个输入字符，以#键结束：')
    if s == '#':
        break
    else:
        str0 += s
with open('writting.txt', 'w') as f:
    f.write(str0)

# 方法二
filename = input('please set a name for the file:')
f = open(filename, 'w')
ch = ''
while '#' not in ch:
    ch = input('please input word by word:')
f.close()
