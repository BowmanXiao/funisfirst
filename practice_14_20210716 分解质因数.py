'''
题目：将一个正整数n分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：1. 应先找到一个最小的质数k（k大于1且小于该数）
2. 将k保存在一个列表中，并用int(n/k)代替原来的n
3. 继续找代替后的n的质数，并保存在列表中
4. 采用一定格式，输出列表中的质因数。
'''
# 方法一 输出格式1
num = int(input("请输入一个大于1的正整数："))
n = num
l = []
while num > 1:
    for i in range(2, num + 1):
        if num % i == 0:
            l.append(i)
            num = int(num / i)
            break
print('%d=' % n + '*'.join([str(x) for x in l]))

# 方法二 输出格式2
x = int(input("是否进入循环？是：1，否：0\n"))
while (x):
    num = int(input("请输入一个大于1的正整数："))
    print('%d=' % num, end='')
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                l.append(i)
                num = int(num / i)
                if num == 1:
                    print(f'{i}', end='')
                else:
                    print(f'{i}*', end='')
                break
    print('')
    x = int(input("是否进入循环？是：1，否：0\n"))
    if x == 0:
        print("循环结束！")
