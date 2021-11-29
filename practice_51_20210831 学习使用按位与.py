'''
题目：学习使用按位与 & 。

程序分析：0&0=0; 0&1=0; 1&0=0; 1&1=1。
'''

# 方法一
if __name__ == '__main__':
    a = 0x12  # 0x为16进制数符号
    b = 0x2F
    print(a & b)  # 0001 0010 & 0010 1111


# 方法二  将两个Bytes连为16bits
def BuildUNIT16(x, y):
    z = 0
    z = x << 8
    z += y
    return z


print('0x%x' % BuildUNIT16(0xaa, 0xf2))  # %d表示输出十进制（dec），%o表示输出八进制（oct），%x表示输出十六进制(hex)
