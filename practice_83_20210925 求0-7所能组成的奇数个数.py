'''
题目：求0—7所能组成的奇数个数，最多n位数。

程序分析：

组成1位数是4个。

组成2位数是7*4个。

组成3位数是7*8*4个。

组成4位数是7*8*8*4个。

......
'''
# 方法一 一般累计算法
def f_ODD(n):
    count = 0
    sum = 0
    for i in range(0, 8):
        if i % 2 == 0:
            count += 1
        count0 = count
    sum += count0
    print(count0)
    for i in range(2, n+1):
        count = 7 * 8 ** (i - 2) * count0
        print(count)
        sum += count
    print(sum)
f_ODD(8)
