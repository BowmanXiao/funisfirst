'''
题目：创建一个链表。

程序分析：无。
'''
# 方法一
if __name__ == '__main__':
    pr = []
    for i in range(5):
        pr.append(int(input('请输入数字：')))
    print(pr)

# 方法二 列表推导式
p = [int(input('Please input a number:')) for i in range(5)]
print(p)
