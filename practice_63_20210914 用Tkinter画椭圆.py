'''
题目：画椭圆。　

程序分析：使用 Tkinter。
'''
if __name__ == '__main__':
    from tkinter import *

    tk = Tk()
    cX = 200  # 初始圆心横坐标
    cY = 260  # 初始圆心纵坐标
    radiusX = 140  # 初始
    radiusY = 140

    canvas = Canvas(tk, width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(cX - radiusX, cY - radiusY, cX + radiusX, cY + radiusY)
        radiusX -= 5
        radiusY += 5
    canvas.pack()
    mainloop()
