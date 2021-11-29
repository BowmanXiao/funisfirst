'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。以抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
程序源代码：
'''

for a in ['x', 'y', 'z']:
    for b in ['x', 'y', 'z']:
        for c in ['x', 'y', 'z']:
            if a != 'x' and c != 'x' and c != 'z' and a != b and b != c and a != c:
                print('a和{}比，b和{}比，c和{}比。'.format(a, b, c))
