'''
题目：画图，学用line画直线。

程序分析：无。
'''

# 方法一
from turtle import *


def drawline(n):
    t = Pen()
    t.color(0.3, 0.8, 0.6)
    t.begin_fill()
    for i in range(n):
        t.speed(1)
        t.forward(50)
        t.left(360 / n)
        t.end_fill()


drawline(10)
exitonclick()

# 方法二
from tkinter import *
root=Tk()
root.title('Polygon')
canvas=Canvas(root,width=400,height=400,bg='green')
canvas.pack()
canvas.create_polygon(290,114,316,114,330,130,     # 使用create_polygon方法绘制六边形
       310,146,284,146,270,130)
canvas.mainloop()
