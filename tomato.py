import time

# 定义常量
WORK_TIME = 25 * 60  # 工作时间（25分钟）
BREAK_TIME = 5 * 60  # 休息时间（5分钟）
LONG_BREAK_TIME = 15 * 60  # 长休息时间（15分钟）
NUM_POMODOROS = 4  # 完成四个番茄周期后休息更长时间

# 开始番茄钟
def start_pomodoro():
    num_pomodoros = 0
    while True:
        # 工作时间
        print("Work for 25 minutes...")
        time.sleep(WORK_TIME)

        # 休息时间
        num_pomodoros += 1
        if num_pomodoros < NUM_POMODOROS:
            print("Take a 5 minute break...")
            time.sleep(BREAK_TIME)
        else:
            print("Take a 15 minute break...")
            time.sleep(LONG_BREAK_TIME)

        # 输出完成的番茄周期数
        print("You have completed", num_pomodoros, "pomodoros.")

# 运行番茄钟
start_pomodoro()
