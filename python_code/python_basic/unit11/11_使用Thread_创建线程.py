import os
import time
# get_native_id:操作系统级别的线程编号，get_ident:python级别的线程编号
from multiprocessing import RLock
from threading import get_native_id, Thread, RLock

# 定义一个 speak 函数，功能是：每隔一秒说话一次
def speak(lock):
    for index in range(5):
        with lock:
            print(f'i am speaking{index}, pid of process is：{os.getpid()}, thread id:{get_native_id()}')
        time.sleep(1)

# 定义一个 study 函数，功能是：每隔一秒学习一次
def study(lock):
    for index in range(5):
        with lock:
            print(f'i am studying {index}, pid of process is: {os.getpid()}, thread id:{get_native_id()}')
        time.sleep(1)


if __name__ == '__main__':
    print(f'-----------start-----------process pid是：{os.getpid()}, thread id:{get_native_id()}')
    lock = RLock()
    t1 = Thread(target=speak, args=(lock, ))
    t2 = Thread(target=study, args=(lock, ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('-----------end-----------')

"""
从头到尾都是一个pid，只有thread是不同的
"""