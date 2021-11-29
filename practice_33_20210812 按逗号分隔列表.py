'''
题目：按逗号分隔列表。
'''
# 方法一 join()函数
l = [1, 2, 3, 4, 5]
s1 = ','.join(str(i) for i in l)
print(s1)

# 方法二 打印格式
l = [1, 2, 3, 4, 5]
for i in l:
    print(i, end='')
    if i != l[-1]:
        print(',', end='')
