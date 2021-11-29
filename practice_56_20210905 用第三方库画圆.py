'''
题目：画图，学用circle画圆形。　　　

程序分析：无。
'''
import turtle, time


# 方法一
def setcanvas():
    turtle.title('画圆')
    turtle.setup(800, 600, 0, 0)
    turtle.color('green')
    turtle.width(5)
    turtle.shape('turtle')


def concentric_circle(radius, gap, number):
    n = gap
    turtle.speed(10)
    turtle.circle(radius)
    turtle.penup()
    turtle.right(90)
    turtle.forward(gap)
    turtle.left(90)
    turtle.pendown()
    for i in range(number - 1):
        turtle.circle(radius + n)
        n += gap
        turtle.penup()
        turtle.right(90)
        turtle.forward(gap)
        turtle.left(90)
        turtle.pendown()


def text():
    turtle.penup()
    turtle.goto(-55, 100)
    time.sleep(0.5)
    turtle.pencolor('red')
    turtle.write('I love you', font=('Arial', 20, 'normal'))


def run():
    setcanvas()
    concentric_circle(100, 10, 4)
    text()
    turtle.mainloop()


if __name__ == '__main__':
    run()

# 方法二
import numpy as np
import matplotlib.pyplot as plt

x = y = np.arange(-11, 11, 0.1)
x, y = np.meshgrid(x, y)
# 圆心为（0，0），半径为1-10
for i in range(1, 11):
    plt.contour(x, y, x ** 2 + y ** 2, [i ** 2])
    # 如果删除下句，得出的图形为椭圆
    plt.axis('scaled')
plt.show()

# 方法三
from tkinter import *

canvas = Canvas(width=800, height=600, bg='yellow')
canvas.pack(expand=YES, fill=BOTH)
k = 1
j = 1
for i in range(0, 35):
    canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
    k += j
    j += 0.3

mainloop()
