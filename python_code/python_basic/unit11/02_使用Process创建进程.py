import os
import time
from multiprocessing import Process, current_process
# current_process 可以直接获取当前进程


# 定义一个 speak 函数，功能是：每隔一秒说话一次
def speak(a, b, msg):
    for index in range(5):
        print(f'{msg}---{a}---{b}---{current_process().name} === i am speaking{index}, pid of process is：{os.getpid()}')
        time.sleep(1)

# 定义一个 study 函数，功能是：每隔一秒学习一次
def study():
    for index in range(5):
        print(f'i am studying {index}, pid of process is: {os.getpid()}')
        time.sleep(1)

# 【必须使用 main 来测试运行，是一个入口】否则，会一直递归调用。
# 一定要写 if __name == '__main__'这个判断，原因如下：
# 1. 当创建子进程时，python 并不会把父进程内存里的 speak 函数直接交给子进程。
# 2. Python会启动一个全新的 python 解释器进程，重新执行当前的 .py文件（作为模块）
# 3. 在执行过程中，重新定义出一个 speak 函数，交给子进程。
if __name__ == '__main__':
    # 创建两个 Process 类的实例对象(进程对象)，分别是p1和p2
    # 注意点1: p1 和 p2 就对应着以后的两个子进程，在创建他们的时候，就要制定好他们要执行的任务。
    # 注意点2: 此时的 p1 和 p2 只是代码层面的两个进程对象，操作系统还没有真的创建 p1 和 p2 两个进程。
    p1 = Process(target=speak, name= 'process of speaking', args=(666, 888), kwargs={'msg': 'jethro'})
    p2 = Process(target=study)

    # 调用进程对象的 start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    # 【顺序不一定按照下面顺序来】
    p1.start()
    p2.start()
