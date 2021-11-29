'''
题目：输出一个随机数。

程序分析：使用 random 模块。
'''
import random

# 生成0到1之间的随机数
print(random.random())
# 生成10到20之间的随机数
print(random.uniform(10, 20))
# 生成10到20之间的随机整数
print(random.randint(10, 20))
# 生成自定义列表中的随机数
print(random.choice([x for x in range(1, 99)]))
