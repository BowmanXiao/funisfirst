'''
题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，
问海滩上原来最少有多少个桃子？

程序分析：假设最后岸上还剩4x只桃子,可以利用递归方法求解。
'''
# 方法一  一般算法
a = 1
n = 1
while a:
    f0 = 4 * a
    for i in range(4):
        f0 = 5 / 4 * f0 + 1
    if f0 % 4 == 0:
        break
    a += 1
f0 = 5 / 4 * f0 + 1
print(a)
print(f'海滩上原来最少有{int(f0)}个桃子。')

# 方法二 递归
num = int(input('请输入猴子的数目：'))


def func(n):
    if n == num:
        return 4 * a
    else:
        return 5 / 4 * func(n + 1) + 1


count = 0
while 1:
    for i in range(1, num):
        if func(i) % 4 == 0:
            count += 1
    if count == num - 1:
        print(f'海滩上原来最少有{int(func(0))}个桃子。')
        break
    a += 1
