'''
题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。
'''
#方法一 赋值数值
#!/usr/bin/python
# -*- coding:utf-8 -*-
a=[1,2,3]
b=a[:]  #将a的数值赋值给b
print(b)
a[0]=5
print('a={},b={}'.format(a,b))  #a变b不变

#方法二 赋值地址
#!/usr/bin/python
# -*- coding:utf-8 -*-
a=[1,2,3]
b=a  #将a的地址赋值给b
print(b)
a[0]=5
print(f'a={a},b={b}')  #a变b变

#方法三 列表生成式
#!/usr/bin/python
# -*- coding:utf-8 -*-
a=[1,2,3]
b=[i for i in a]  #列表生成式
print(b)

#方法四 for循环
#!/usr/bin/python
# -*- coding:utf-8 -*-
a=[1,2,3]
b=[]
c=[]
for i in range(len(a)):
    b.append(a[i])
for i in a:
    c.append(i)
print(b)
print(c)