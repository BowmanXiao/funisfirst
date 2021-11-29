'''
题目：列表转换为字典。

程序分析：无。
'''
# 方法一 dict()函数
lis1 = ['小明', [26, 180]]
lis2 = ['小刚', [28, 175]]
print(dict([lis1, lis2]))

# 方法二 zip()函数
lis1 = ['小明', '小刚']
lis2 = [26, 28]
print(dict(zip(lis1, lis2)))

# 方法三 赋值
lis1 = ['小明', '小刚']
lis2 = [26, 28]
d = {}
for i in range(len(lis1)):
    d[lis1[i]] = lis2[i]
print(d)

# 方法四 字典推导式
lis1 = ['小明', '小刚']
lis2 = [26, 28]
print({lis1[i]: lis2[i] for i in range(len(lis1))})
