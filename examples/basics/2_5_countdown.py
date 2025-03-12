# 简单的倒计时计时器
import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time left: {i} seconds")
        time.sleep(1)
    print("Time's up!")

countdown(5)  # 5秒倒计时
