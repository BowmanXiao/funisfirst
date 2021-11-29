'''
题目：对10个数进行排序。

程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
尤其需要注意10个数中存在重复值的情况。
'''

# 程序一：对无重复数字的固定10个数进行排序
num = [1,5,8,7,2,4,3,9,6,10]
for i in range(9):
    if num[i] > min(num[i + 1:10]):
        j = num.index(min(num[i + 1:10]))
        num[i], num[j] = num[j], num[i]
print(num)

# 程序二：对有重复数字的固定10个数进行排序
num = [1,5,8,7,1,4,3,9,7,10]
for i in range(9):
    if num[i] > min(num[i + 1:10]):
        if min(num[i + 1:10]) in num[:i + 1]:  # 列表中存在相同数的情况
            j_index = []
            for m, n in enumerate(num):  # 通过for循环遍历由enumerate()函数获取的列表的（索引，值）
                if n == min(num[i + 1:10]) and m > i:  # 通过if条件筛选出需要的索引，并添加到自定义索引列表y_index[]中
                    j_index.append(m)
            num[i], num[j_index[0]] = num[j_index[0]], num[i]
        else:
            j = num.index(min(num[i + 1:10]))  # 列表中不存在相同数的情况
            num[i], num[j] = num[j], num[i]
print(num)

# 程序三：对任意输入的n个数进行排序
num = list(map(int, input("请连续输入几个数，按单个空格隔开：").split(' ')))
l=len(num)
for i in range(l-1):
    if num[i] > min(num[i + 1:l]):
        if min(num[i + 1:l]) in num[:i + 1]:  # 列表中存在相同数的情况
            j_index = []
            for m, n in enumerate(num):  # 通过for循环遍历由enumerate()函数获取的列表的（索引，值）
                if n == min(num[i + 1:l]) and m > i:  # 通过if条件筛选出需要的索引，并添加到自定义索引列表y_index[]中
                    j_index.append(m)
            num[i], num[j_index[0]] = num[j_index[0]], num[i]
        else:
            j = num.index(min(num[i + 1:l]))  # 列表中不存在相同数的情况
            num[i], num[j] = num[j], num[i]
print(num)