'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

程序分析：无
'''
hei = int(input("请输入初始高度："))  # 可改为常量100
tim = int(input("请输入第几次反弹："))  # 可改为常量10
height = []
tour = []
for i in range(1, tim + 1):
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei = hei / 2
    height.append(hei)
print('它在第{}次落地时，共经过{}米'.format(tim, sum(tour)))
print('第{}次反弹高度为{}'.format(tim, height[-1]))
