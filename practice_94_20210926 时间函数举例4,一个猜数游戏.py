'''
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。

程序分析：无。
'''
import time
import random

while True:
    play_it = input('You wanna play the game?(\'y\' or \'n\')')
    if play_it == 'y':
        n = random.randint(0, 1000)
        guess = int(input('input your guess (0~1000):'))
        start = time.time()
        while 1:
            if guess > n:
                guess = int(input('guess a smaller number:'))
            elif guess < n:
                guess = int(input('guess a bigger number:'))
            else:
                print('Bingo!')
                print('Congratulations!')
                end = time.time()
                break
        rec = end - start
        print(f'Your reaction time is {rec}s.')
        if rec < 25:
            print('You are smart!')
        elif rec < 40:
            print('You are normal!')
        else:
            print('You are stupid!')
    else:
        print('Think again?')
