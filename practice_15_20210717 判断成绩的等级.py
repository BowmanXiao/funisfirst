'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''
# 方法一 简单if分支
score = int(input("请输入分数："))
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")

# 方法二 三目表达式
score = int(input("请输入分数："))
print('A' if score >= 90 else ('B' if score >= 60 else 'C'))

# 方法三 列表
scores = [90, 60, 0]
grades = ['A', 'B', 'C']
# score = int(input("请输入分数："))
score_list = [90, 100, 50, 67, 40, 60]
for score in score_list:
    for i in range(3):
        if score >= scores[i]:
            print(f'{score}为{grades[i]}等级')
            break


# 方法四 range函数
def Grade(score):
    if score in range(60):
        print("C")
    elif score in range(60, 90):
        print("B")
    else:
        print("A")


score = int(input("请输入分数："))
Grade(score)
