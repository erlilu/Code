CPU密集型任务---适合使用多进程（大部分时间花在“算”上）【图像处理、视频编码/解码、数值计算、模型训练】

I/O密集型任务---适合使用多线程（大部分时间花在“等”上）【文件I/O、网络请求、操作数据库】

#  进程相关
1. 相关概念：并发并行、同步异步、进程线程
2. 进程之间不共享内存，因此也就不共享任何变量。


# Process
**基础代码**
```python
import os
import time
from multiprocessing import Process, current_process
# current_process 可以直接获取当前进程


# 定义一个 speak 函数，功能是：每隔一秒说话一次
def speak():
    for index in range(10):
        print(f'i am speaking{index}, pid of process is：{os.getpid()}')
        time.sleep(1)

# 定义一个 study 函数，功能是：每隔一秒学习一次
def study():
    for index in range(15):
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
    p1 = Process(target=speak)
    p2 = Process(target=study)

    # 调用进程对象的 start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    # 【顺序不一定按照下面顺序来】
    p1.start()
    p2.start()
```
## Process的参数
- group: 默认值为None（应当始终为None）
- target: 子进程要执行的课调用对象，默认值为 None
- name: 进程名称，默认值为 None，如果设置为 None，python会自动分配名字。
- args: 给target传的位置参数（元组）
- kwargs: 给 target 传的关键子参数（字典）
- daemon: 标记进程是否为**守护进程**，去值为布尔值（默认值为 None，表示从创建方进程继承）

```python
import os
import time
from multiprocessing import Process, current_process

def speak(a, b, msg):
    for index in range(5):
        print(
            f'{msg}---{a}---{b}---{current_process().name} === i am speaking{index}, pid of process is：{os.getpid()}'
        )
        time.sleep(1)
        
    p1 = Process(target=speak, name= 'process of speaking', args=(666, 888), kwargs={'msg': 'jethro'})
```

## Lock 
问题：当在运行经典代码时，不同的进程，会存在**争抢控制台**的情况。
解决：上锁Lock
- 引入RLock， 避免多次上锁无法解开
推荐写法
```python
import multiprocessing 
from multiprocessing import Process, Lock, RLock
import time

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
    lock = Lock()
    p = Process(target=study, args=(lock, ))
    p.start()
```

## join
1. join方法的作用：阻塞当前进程，等 join 前面的进程执行完，再继续往下执行。
2. join(timeout), 其中 timeout 是可选参数，表示等多久，单位是秒。

注意点：
1. p.join() 不是让进程 p 等，而是让“执行这行 join 代码的那个进程”去等，等的是p这个进程
2. 当达到了 timeout 所指定的时间后，进程并不会终止，只是“不再等”了
3. join 必须在 start 之后


### Lock_test.py 报错
- 问题根源：锁的“上下文”不匹配
你的报错 self._semlock = _multiprocessing.SemLock._rebuild(*state) FileNotFoundError，
本质是 fork 上下文创建的锁，被传递给了 spawn 上下文的进程。
spawn 的子进程无法继承父进程的文件句柄，因此找不到这个锁对应的底层文件，导致 _rebuild 失败
- 解决方案：统一使用 spawn 上下文
  - 写法一：使用 get_context('spawn')【推荐】
  - 写法二：全局设置 start_method


## terminate
p1.terminate()      # 终止，但没有结束进程，is_alive()=True

## 守护进【daemon】
1. 一种依附于主进程存在的子进程，一旦住进程结束，它就会被自动终止。
2. 简言之：主进程一死，守护进程必须跟着死。

应用场景
- 后台监控类任务
- 日志 / 统计 / 采样  类任务
- 辅助型‘陪跑任务’

注意点：
1. 守护进程必须是 子进程。
2. 主进程结束，守护进程也会随之结束。
3. 守护进程中，不允许再创建新的子进程。
4. 必须在 start 之前，start()之后，不能再设置 daemon


# Queue 队列
1. list,tuple,dict，特点：数据随意拿取
2. 队列Queue：一种“先进先出”的数据结构（先放进去的数据，一定会先取出来）
## Queue 队列常用方法
1. get()
2. put()
3. empty()
4. full()
5. qsize()

## 队列具备等待模式
### 【put】
1. 当队列已满，继续put，就会进入等待模式，等别人调用get方法，取走一个元素
2. 当队列已满，执行：put(元素， timeout=秒数)，就会等待指定秒数。
3. put_nowait()：会直接向队列中添加元素，不会进入等待模式。若队列已满，会抛出异常。
【备注：put_nowait 等价于 put(元素, block=False), block的默认值为 True】

### 【get】
> get 读多了，也会进入等待模式
1. 当队列已空，继续get，就会进入等待模式。
2. 当队列已空，执行get(timeout=秒数)，就会等待制定秒数。
3. get_nowait()：会直接读取队列中的元素，不会等待模式，若队列已空，会抛出异常。
【备注：get_nowait 等价于 get(block=False)】
```python
from multiprocessing import Queue

# 创建一个队列(不限制容量上限）
q1 = Queue()
# 创建一个队列(限制容量上限）
q2 = Queue(3)

# 1. put方法：放入数据（入队）
q1.put(10)
q1.put(20)
q1.put(30)
# 2. get方法：取出数据（出队）
value1 = q1.get()
value2 = q1.get()
value3 = q1.get()

# 3. empty方法：判断队列是否为空[bool]
result1 = q1.empty()
# 4. full方法：判断队列是否为满[bool]
result2 = q1.full()
# 5. qsize方法：获取队列长度
queue_size = q2.qsize()

# 6. 队列具备等待模式
```

## 使用Queue来进行进程间的通信
但一定要注意**引用的包**的方式:
from multiprocessing import Process, Queue

# 使用Pipe来进行进程间的通信
1. 管道是双向的，两边都可以传输和接收数据。
2. Pipe(duplex=True),默认值是True；如果duplex=False，变成了单向，一端只能发送，另一端只能接收。
3. 单向时：con1为只能接收，con2为只能发送。【先接收，再发送】

# 继承Process创建进程
[09_继承Process.py]

# 进程池 ProcessPoolExecutor
1. 创建「进程池执行器」、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。
2. **获取子进程执行后的返回结果**(Future类的实例对象 + result方法)。
3. 使用 as_completed: 按“完成顺序”获取结果。
4. 使用 add_done_callback 方法，为任务添加完成时的回调函数。
5. 使用 map 方法批量提交任务(注意：map方法是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的)
6. 使用 with：进程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)

# 使用Thread创建线程
## Thread 的参数【与Process参数一致】
- group: 默认值为None（应当始终为None）
- target: 子进程要执行的课调用对象，默认值为 None
- name: 进程名称，默认值为 None，如果设置为 None，python会自动分配名字。
- args: 给target传的位置参数（元组）
- kwargs: 给 target 传的关键子参数（字典）
- daemon: 标记进程是否为**守护进程**，去值为布尔值（默认值为 None，表示从创建方进程继承）：


# GIL(global interpreter lock)全局解释器锁
> 无论CPU有多少个核心，在某一时刻，只允许进程中的一个线程去执行 Python 代码。
- GIL是CPython 解释器中的一把互斥锁
- GIL锁的作用：无论CPU有多少个核心，在某一时刻，只允许同一个进程中的一个线程去执行python代码

## 何时释放GIL锁
1. 主动释放（遇到I/O操作）
2. 被迫释放（任务超时）
CPython解释器中的多线程模型，本质上是并发，而不是并行！（是快速切换，而不是同时进行）
【这种设计———— 为了确保解释器级别的数据安全】

## GIL锁和编码时使用的 Lock 和 Rlock 不是一个东西。
- Lock 和 Rlock 时业务层面的锁，目标是：让业务逻辑别出错


