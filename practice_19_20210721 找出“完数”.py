'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''
# 方法一 直接求解
for num in range(2, 1001):
    sum = 0
    item = []
    for i in range(1, num):
        if num % i == 0:
            sum += i
            item.append(i)
    if sum == num:
        print('%d=' % num + '+'.join([str(x) for x in item]) + '，为完整数')


# 方法二 函数
l=[]
def get_num(num):
    sum = 0
    item = []
    for i in range(1, num):
        if num % i == 0:
            sum += i
            item.append(i)
    if sum == num:
        print('%d=' % num + '+'.join([str(x) for x in item]) + '，为完整数')
        l.append(num)
for num in range(2, 1001):
    get_num(num)
print(l)
