'''
题目：放松一下，算一道简单的题目。

程序分析：无。
'''
import time
if __name__=='__main__':
    date=time.strftime('%m-%d', time.localtime())
    if date=='02-14':
        print('情人节，是时候给你女朋友买束玫瑰花了！')
    else:
        print('这时候你不要忘记发个红包！')
    print('哈哈，这是一个测试题~')