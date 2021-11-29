'''
题目：找到年龄最大的人，并输出。请找出程序中有什么问题。

程序分析：无。
'''
# 方法一
if __name__ == '__main__':
    person = {'li': 20, 'wang': 35, 'zhang': 68, 'sun': 16}
    man = 'li'
    man2 = 'li'
    for key in person.keys():
        if person[man] < person[key]:
            man = key
        if person[man2] > person[key]:
            man2 = key
    print('年龄最大者是{}，{}岁'.format(man, person[man]))
    print('年龄最小者是{}, {}岁'.format(man2, person[man2]))

# 方法二
person = {'li': 20, 'wang': 35, 'zhang': 68, 'sun': 16}
maxValue = max(person.values())
minValue = min(person.values())
for key in person.keys():
    if person[key] == maxValue:
        print(key, maxValue)
    if person[key] == minValue:
        print(key, minValue)
