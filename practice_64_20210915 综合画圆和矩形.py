'''
题目：利用ellipse 和 rectangle 画图。。　

程序分析：无。
'''
if __name__=='__main__':
    from tkinter import *
    root=Tk()
    canvas=Canvas(root, width=400, height=400, bg='yellow')
    canvas.pack()
    x0=100
    y0=100
    rx=20
    ry=20
    for i in range(5):
        canvas.create_oval(x0-rx, y0-ry, x0+rx, x0+ry)
        canvas.create_oval(x0-20, y0-ry, x0+20, y0+ry)
        rx+=5
        ry+=5
        canvas.create_rectangle(2*x0-rx, 2*y0-ry, 2*x0+i*rx, 2*x0+i*ry)
    root.mainloop()


