import os
import time
from multiprocessing import Process

# 定义一个监控【】
def monitor():
    while True:
        try:
            with open('log.txt', 'r+') as f:
                lines = sum(1 for _ in f)
        except FileNotFoundError:
            lines = 0
        print(f'【守护进程】{os.getpid()},the log.txt file is {lines} lines')
        time.sleep(1)

if __name__ == '__main__':
    print(f'i am the main process {os.getpid()} the first code of line')

    p = Process(target=monitor, daemon=True)
    p.start()

    # 向文件中写入数据
    with open('log.txt','a+', encoding='utf-8') as f:
        for index in range(10):
            f.write(f' this is {index}\n')
            f.flush()
            time.sleep(1)
    print(f'i am the main process {os.getpid()} the least code of line')
    print('sucessed!')


