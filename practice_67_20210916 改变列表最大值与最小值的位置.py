'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

程序分析：无。
'''

# 方法一
a = [1, 8, 7, 6, 4, 5, 9, 3, 2]
a.sort()
for i in range(len(a)):
    if a[i] == max(a):
        a[0], a[i] = a[i], a[0]
    if a[i] == min(a):
        a[len(a) - 1], a[i] = a[i], a[len(a) - 1]
print(a)

# 方法二
a = [1, 8, 7, 6, 4, 5, 9, 3, 2]
max0 = 0
min0 = 0
for i in range(len(a)):
    if a[i] > a[max0]:
        max0 = i
    if a[i] < a[min0]:
        min0 = i
if min == 0:
    a[0], a[max0] = a[max0], a[0]
    a[len(a) - 1], a[max0] = a[max0], a[len(a) - 1]
else:
    a[0], a[max0] = a[max0], a[0]
    a[len(a) - 1], a[min0] = a[min0], a[len(a) - 1]
print(a)

# 方法三
a = [1, 8, 7, 6, 4, 5, 9, 3, 2]


def arr_max(a):
    max0 = 0
    for i in range(len(a)):
        if a[i] > a[max0]:
            max0 = i
    a[0], a[max0] = a[max0], a[0]


def arr_min(a):
    min0 = 0
    for i in range(len(a)):
        if a[i] < a[min0]:
            min0 = i
    a[len(a) - 1], a[min0] = a[min0], a[len(a) - 1]


if __name__ == '__main__':
    arr_max(a)
    arr_min(a)
    print(a)

# 方法四
a = [1, 8, 7, 6, 4, 5, 9, 3, 2]

def exchang_max(a):
    max0 = 0             # 命名的时候注意不能和使用的系统函数重名，如max和max()，否则会报错 not callable，切记！
    max0 = max(a)
    a.remove(max0)
    a.insert(0, max0)


def exchang_min(a):
    min0 = 0
    min0 = min(a)
    a.remove(min0)
    a.append(min0)

def pr(a):
    for i in a:
        print(i, end=' ')

def run(a):
    exchang_max(a)
    exchang_min(a)
    pr(a)

if __name__ == '__main__':
    run(a)

