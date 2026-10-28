import multiprocessing
import time
import os
from multiprocessing import Process, Lock


def speak(lock):
    for _ in range(10):
        # 上锁：如果锁是空闲的，立刻上锁，继续往下执行；如果锁被别人拿着：当前进程会阻塞等待(原地)
        lock.acquire()
        print('好好', end='')
        print('学习', end='')
        print('天天', end='')
        print('向上')
        # 解锁：acquire 和 release 必须成对出现，否则会永远卡住(死等)
        lock.release()
        time.sleep(1)

def study(lock):
    for _ in range(10):
        # with lock: 会自动完成两件事“
        # 1. 进入前：自动执行lock.acquire()
        # 2. 离开后：自动执行lock.release()
        # 优势：即便代码块里发生异常，也能保证释放锁，避免“卡斯”
        with lock:              #【推荐写法】
            print('A', end='')
            print('B', end='')
            print('C', end='')
            print('D')
        time.sleep(1)

if __name__ == '__main__':
    print('i am the main process that the first lien will print')
    # 1. 获取 spawn 上下文
    ctx = multiprocessing.get_context('spawn')
    # 2. 用同一个上下文创建锁和进程
    lock = ctx.Lock()
    p1 = Process(target=speak, args=(lock, ))
    p2 = Process(target=study, args=(lock, ))
    # 3. 在start()之后调用join()，确保住进程等待子进程完成。【阻塞进程】
    p1.start()
    # 让主进程等 p1 进程执行完毕之后，主进程再继续执行
    p1.join()

    p2.start()
    # 让主进程等 p2 进程执行完毕后，主进程再继续执行
    p2.join()


