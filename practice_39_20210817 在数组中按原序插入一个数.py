'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
'''

# 方法一 for循环加if函数进行判断
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
b = 18
a.append(b)
for i in range(len(a), 0, -1):
    if a[i - 1] < a[i - 2]:
        m = a[i - 1]
        a[i - 1] = a[i - 2]
        a[i - 2] = m
    else:
        break
print(a)

# 方法二 insert()函数
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
b = 28
for i in range(len(a)):
    if i==len(a)-1:
        a.append(b)
    elif b >= a[i] and b <= a[i + 1]:
        a.insert(i + 1, b)
        break

print(a)

# 方法三 sort()函数
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
b = 18
a.append(b)
print(sorted(a), a)  # sorted()会返回一个列表，而原列表不变
print(a.sort(), a)  # sort()函数是直接在原来的基础上修改。reversed()和reverse()用法同理
