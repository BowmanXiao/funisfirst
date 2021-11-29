'''
题目：编写input()和output()函数输入，输出5个学生的数据记录。

程序分析：无。
'''
# 方法一 面向过程
N = 2
student = []
for i in range(N):
    student.append(['', '', []])


def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('请输入学生编号：')
        stu[i][1] = input('请输入学生姓名：')
        for j in range(3):
            stu[i][2].append(int(input('请依次输入各科成绩：')))


def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' % (stu[i][0], stu[i][1]))
        for j in range(3):
            print('%-8d' % stu[i][2][j])


if __name__ == '__main__':
    input_stu(student)
    output_stu(student)


# 方法二 面向对象
class student():
    def __init__(self, N):
        self.N = N
        self.student = []
        for i in range(self.N):
            self.student.append(['', '', []])

    def input_stu(self):
        for i in range(self.N):
            self.student[i][0] = input('请输入学生编号：')
            self.student[i][1] = input('请输入学生姓名：')
            for j in range(3):
                self.student[i][2].append(int(input('请依次输入各科成绩：')))

    def output_stu(self):
        for i in range(self.N):
            print('%-6s%-10s' % (self.student[i][0], self.student[i][1]))
            for j in range(3):
                print('%-8d' % self.student[i][2][j])


student = student(3)
student.input_stu()
student.output_stu()
