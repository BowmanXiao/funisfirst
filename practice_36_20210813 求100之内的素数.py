'''
题目：求100以内的素数。

程序分析：设置两个for循环，一个循环赋值1~100的数，一个循环判断是否为素数。
'''
# 方法一
l = []
for num in range(1, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        l.append(num)
print(l)

# 方法二
l = []
for num in range(1, 101):
    if 0 not in [num % i for i in range(2, num)]:
        l.append(num)
print(l)


