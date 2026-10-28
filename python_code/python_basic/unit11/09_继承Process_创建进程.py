import os
import time
from multiprocessing import Process, Lock

"""
A1: 两个进程的输出出现在同一行。

- 根本原因：主进程、SpeakProcess 和 StudyProcess 是三个独立的进程，它们各自向同一个终端（stdout）写入，操作系统不保证写入的原子性。
- 当两个进程几乎同时执行 print 时，输出就会交错、挤在同一行。

✅ 解决方法：用 multiprocessing.Lock 串行化打印。
给两个进程共享一把锁，谁要打印就先拿锁，打印完再释放。这样同一时刻只有一个进程能写终端。

🎯 关键改动说明

1. 重写 __init__：Process 的子类如果要接收参数，必须调用 super().__init__()，否则会报错。
2. 共享锁：锁在主进程中创建，作为参数传给两个子进程。这样它们用的是同一把锁。
3. with self.lock: ：等价于 acquire() + release()，但更安全，即使打印出错也会自动释放锁。

"""
class SpeakProcess(Process):
    # 初始化方法设置可传递参数。一定要继承一下：super().__init__()
    def __init__(self, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)       # 继承函数传参
        self.lock = lock

    def run(self):
        for index in range(10):
            with self.lock:
                print(f'【Speak】index---{index}, pid---{os.getpid()}, ppid---{os.getppid()}')
            time.sleep(1)


class StudyProcess(Process):
    def __init__(self, lock):
        super().__init__()
        self.lock = lock

    def run(self):
        for index in range(10):
            with self.lock:
                print(f'【Study】index---{index}, pid---{os.getpid()}, ppid---{os.getppid()}')
            time.sleep(1)

if __name__ == '__main__':
    print('The main process will print the 【first】 line ')

    lock = Lock()               # 创建共享锁
    # 不需要传值
    p1 = SpeakProcess(lock)
    p2 = StudyProcess(lock)

    # 不可以调用run() 方法，不然进程是同一个；
    # start() 方法：2步 ———— 向os请求进程 --> 执行run()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('The main process will print the 【last】 line ')

