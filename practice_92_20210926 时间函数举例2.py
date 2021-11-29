'''
题目：时间函数举例2。

程序分析：无。
'''
import time

start = time.time()
print(start)
for i in range(10000):
    print(i)
end = time.time()
print(end)
print(f'共花费{end - start}s.')
