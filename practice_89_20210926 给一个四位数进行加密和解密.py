'''
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

程序分析：无。
'''


# 加密
def encode(num):
    num = str(num)
    lis = []
    for i in num:
        lis.append(str((int(i) + 5) % 10))
    for i in range(2):
        lis[i], lis[3 - i] = lis[3 - i], lis[i]
    value = ''.join(lis)
    print(f'{num} 加密后为：{value}')


encode(1574)


# 解密
def decode(num):
    num = str(num)
    lis = []
    for i in num:
        if int(i) >= 0 and int(i) <= 4:
            lis.append(str(int(i) + 10 - 5))
        else:
            lis.append(str(int(i) - 5))
    lis.reverse()
    key = ''.join(lis)
    print(f'{num} 加密前为：{key}')
decode(9206)
