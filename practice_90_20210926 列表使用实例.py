'''
题目：列表使用实例。

程序分析：无。
'''
lis = [10010, '中国联通', [1, 2, 3, 4, 5]]
print(len(lis))  # 访问列表长度
print(lis[1:])  # 到列表结尾
lis.append('I\'m new here!')  # 向列表添加元素
print(len(lis))
print(lis[-1])  # 输出列表最后一个元素
print(lis.pop())  # 弹出列表最后一个元素
print(len(lis))
print(lis)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[1])

col2 = [row[1] for row in matrix]  # 输出矩阵的某一列
print(col2)
col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # 输出某一列的偶数
print(col2even)
