'''
题目：使用lambda来创建匿名函数。

程序分析：无
'''
# 方法一
maxN = lambda x, y: (x > y) * x + (x < y) * y
minN = lambda x, y: (x > y) * y + (x < y) * x
print('较大值为{}'.format(maxN(1, 3)))
print('较小值为{}'.format(minN(1, 3)))

# 方法二
print(list(filter(lambda x: x ** 2 < 50, range(1, 10))))
