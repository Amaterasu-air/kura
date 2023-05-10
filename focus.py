import time
import os

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        os.system('clear')  # 清屏
        print('Focus on your work for the next {} minutes.'.format(minutes))
        print('Time remaining: {} seconds'.format(seconds))
        time.sleep(1)
        seconds -= 1
    os.system('clear')  # 清屏
    print('Time is up! Take a break.')

# 专注时长为25分钟
focus_timer(25)
