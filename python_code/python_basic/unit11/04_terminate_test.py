import multiprocessing
import time
import os
from multiprocessing import Process, Lock
from os import lockf
from time import process_time_ns


def speak(lock):
    for _ in range(10):
        with lock:
            print('好好', end='')
            print('学习', end='')
            print('天天', end='')
            print('向上')
        time.sleep(1)

def study(lock):
    for _ in range(10):
        with lock:              #【推荐写法】
            print('A', end='')
            print('B', end='')
            print('C', end='')
            print('D')
        time.sleep(1)

if __name__ == '__main__':
    print('i am the main process that [the first] lien will print')
    # 1. 获取 spawn 上下文
    ctx = multiprocessing.get_context('spawn')
    # 2. 用同一个上下文创建锁和进程
    lock = ctx.Lock()
    p1 = Process(target=speak, args=(lock, ))
    p2 = Process(target=study, args=(lock, ))
    p1.start()
    p2.start()

    time.sleep(5)
    print('i am the main process, i will terminate p1......')
    p1.terminate()      # 终止，但没有结束进程，is_alive()=True
    p1.join()           # 真正的结束，is_alive() = false
    print(p1.is_alive())

    print('i am the main process that [the least] lien will print')



