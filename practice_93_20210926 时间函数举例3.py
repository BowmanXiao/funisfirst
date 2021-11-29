'''
题目：时间函数举例3。

程序分析：无。
'''
import time

start = time.process_time()
print(start)
print(time.time())
for i in range(10000):
    print(i, end=' ')
print()
end = time.process_time()
print(end)
print(end-start)
