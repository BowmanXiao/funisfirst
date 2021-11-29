'''题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。

程序源代码：
'''
#方法一：直接输出
#!/usr/bin/python
# -*- coding: UTF-8 -*-
num=0
for i in range(1,5):
  for j in range(1,5):
      for k in range(1,5):
          if i!=j and i!=k and j!=k:
              num+=1
              print(str(i)+str(j)+str(k),end=' ')
print("方法一：共能组成{}个互不相同且无重复数字的三位数。".format(num))
print('')

#方法二：添加到列表后输出
#!/usr/bin/python
# -*- coding:UTF-8 -*-
num=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                num.append((str(i)+str(j)+str(k)))
print("方法二：共能组成{}个互不相同且无重复数字的三位数。".format(len(num)))
for i in num:
    print(i,end=" ")
print('\n')

#方法三：排列组合
tar=['1','2','3','4']
d=[]
num=0
for i in range(len(tar)):
    n1=tar.pop(i)
    for j in range(len(tar)):
        n2=tar.pop(j)
        for k in range(len(tar)):
            n3=tar[k]
            d.append(n1+n2+n3)
            num+=1
        tar.insert(j,n2)
    tar.insert(i,n1)
print("方法三：一共能组成{}个相同且无重复数字的三位数，分别为：".format(num))
for i in d:
    print("{}".format(i),end=' ')