'''
题目：反向输出一个链表。

程序分析：无。
'''
import random
# 方法一 reverse()函数
p = [random.randint(1, 100) for i in range(5)]
print(p)
p.reverse()
print(p)
print()

# 方法二 倒序输出
p = [random.randint(1, 100) for i in range(5)]
print(p)
print(p[::-1])
print()

# 方法三 滚动列表
p = [random.randint(1, 100) for i in range(5)]
print(p)
for i in range(4):
    p.insert(i, p.pop())
print(p)