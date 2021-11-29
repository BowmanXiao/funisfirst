'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。
'''
# 方法一 多参数赋值，for循环
n = int(input("请输入求和的项数："))
sum = 0
a = 1
b = 2
for i in range(n):
    item = b / a
    sum += item
    a, b = b, a + b
print('前%d项之和为：%s' % (n, sum))


# 方法二  一般赋值，定义函数
def Get_sum(n):
    print('前{}项之和为：'.format(n), end='')
    sum = 0
    a = 1
    b = 2
    while n > 0:
        sum += b / a
        q = a
        a = b
        b = q + b
        n -= 1
    print(sum)
Get_sum(20)
