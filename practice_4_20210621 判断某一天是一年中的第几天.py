'''
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

程序源代码：
'''
# 方法一
#!/usr/bin/python
# -*- coding: UTF-8 -*-
year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))
months=(0,31,59,90,120,151,181,212,243,273,304,334)
if 0<month<=12:
    sum=months[month-1]+day
else:
    print('data error!')
leap=0
if year%400==0 or year%4==0 and year%100!=0:
    leap=1
if leap==1 and month>2:
    sum+=1
print('It is the %d day'%sum)

# 方法二
#!/usr/bin/python
# -*- coding: UTF-8 -*-
year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))
months1=(0,31,59,90,120,151,181,212,243,273,304,334)
months2=(0,31,60,91,121,152,182,213,244,274,305,335)
if 0<month<=12:
    if year%400==0 or year%4==0 and year%100!=0:
        Dth=months2[month-1]+day
    else:
        Dth=months1[month-1]+day
else:
    print('data error!')
print('It is the %d day'%Dth)

# 方法三
#!/usr/bin/python
# -*- coding: UTF-8 -*-
year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))
months1=(0,31,59,90,120,151,181,212,243,273,304,334)
months2=(0,31,60,91,121,152,182,213,244,274,305,335)
if 0<month<=12:
    if year%4==0:
        if year%100==0 and year%400!=0:
            Dth=months1[month-1]+day
        else:
            Dth=months2[month-1]+day
    else:
        Dth = months1[month - 1] + day
else:
    print('data error!')
print('It is the %d day'%Dth)

# 方法四
#!/usr/bin/python
# -*- coding: UTF-8 -*-
year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if 0<month<=12:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        days[2]+=1
    Dth=sum(days[0:month])+day
else:
    print('data error!')
print('It is the %d day'%Dth)

# 方法五
#!/usr/bin/python
# -*- coding: UTF-8 -*-
year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if 0<month<=12:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        days[2]+=1
    for each in range(0,month):
        day+=days[each]
else:
    print('data error!')
print('It is the %d day'%day)