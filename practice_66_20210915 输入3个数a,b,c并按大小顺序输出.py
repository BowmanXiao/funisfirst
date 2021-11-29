'''
题目：输入3个数a,b,c，按大小顺序输出。　　　

程序分析：无。
'''
# 方法一 sort()函数
a=list(map(int, input('请输入三个整数：').split(' ')))
a.sort(reverse=False)
print(a)

# 方法二 if判断
x=int(input('输入第一个数：'))
y=int(input('输入第二个数：'))
z=int(input('输入第三个数：'))
if x>y:
    x,y=y,x
if y>z:
    y,z=z,y
if x>z:
    x,z=z,x
print(x,y,z)

# 方法三 冒泡排序
a=[2,5,9,7,4,5,3,5,8,4]
for i in range(len(a)-1):  # 10个数需循环9遍，每一遍排好一个局部最大数，留下最后一个即为最小数
    for j in range(len(a)-1-i):  # 一个循环后，最大数排在了列表最后，下一次循环不用再排这些数，因此要减去i
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)