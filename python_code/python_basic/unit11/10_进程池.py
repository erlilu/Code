import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# 1.创建进程池执行器、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成
# region
# def work(n):
#     print(f'work is doing task{n}......{os.getpid()}')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     print('--------start--------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     # 使用 submit 方法提交任务
#     executor.submit(work, 1)
#     executor.submit(work, 2)
#     executor.submit(work, 3)
#     executor.submit(work, 4)
#     executor.submit(work, 5)
#     executor.submit(work, 6)
#     executor.submit(work, 7)
#     # shutdown 的作用：不再接收新的任务
#     # wait=True 的作用：阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#
#     print('--------end--------')
"""
进程池当前进程任务过于简单，完全可以单一进程完成
"""
# endregion

# 2. 获取子进程执行后的返回结果(Future类的实例对象 + result方法)
# region
# def work(n):
#     print(f'work is doing task{n}......{os.getpid()}')
#     time.sleep(1)
#     return f'this is task result of {n}'
#
# if __name__ == '__main__':
#     print('--------start--------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     # 使用 submit 方法提交任务(submit 只负责“提交任务”，不会阻塞主进程)
#     # future1 = executor.submit(work, 1)
#     # future2 = executor.submit(work, 2)
#     # future3 = executor.submit(work, 3)
#     # future4 = executor.submit(work, 4)
#     # future5 = executor.submit(work, 5)
#     # future6 = executor.submit(work, 6)
#     # future7 = executor.submit(work, 7)
#     futures = [executor.submit(work, n) for n in range(7)]
#     # shutdown 的作用：不再接收新的任务
#     # wait=True 的作用：阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#
#     # result() 是会阻塞的。【必须等 submit 之后再给结果】
#     # print(future1.result())
#     # print(future2.result())
#     # print(future3.result())
#     # print(future4.result())
#     # print(future5.result())
#     # print(future6.result())
#     # print(future7.result())
#     for f in futures:
#         print(f.result())
#     print('--------end--------')
# endregion

# 3. 使用 as_completed: 按“完成顺序”获取结果
# region
# def work(n):
#     print(f'work is doing task{n}......{os.getpid()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'this is task result of {n}'
#
# if __name__ == '__main__':
#     print('--------start--------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#     # 使用 submit 方法提交任务(submit 只负责“提交任务”，不会阻塞主进程)
#     futures = [executor.submit(work, n) for n in range(1, 8)]
#
#     # 准备一个 result_list 去收集任务的具体结果
#     result_list = []
#     # 收集每个任务的结果
#     for f in as_completed(futures):
#         result_list.append(f.result())
#
#     # shutdown 的作用：不再接收新的任务
#     # wait=True 的作用：阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     # 打印最终的结果
#     print(result_list)
#     print('--------end--------')
# endregion

# 4. 使用 add_done_callback 方法，为任务添加完成时的回调函数
# region
# def work(n):
#     print(f'work is doing task{n}......{os.getpid()}')
#     time.sleep(1)
#     return f'this is task result of {n}'
#
# if __name__ == '__main__':
#     print('--------start--------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#
#     # 准备一个 result_list 列表去收集任务的结果
#     result_list = []
#
#     # 任务完成后的回调函数
#     def done_func(future):
#         result_list.append(future.result())
#     # 开启7个任务，并制定回调函数
#     for index in range(1, 8):
#         f = executor.submit(work, index)
#         f.add_done_callback(done_func)
#
#     # shutdown 的作用：不再接收新的任务
#     # wait=True 的作用：阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#
#     # 按照完成的顺序获取
#     print(result_list)
#     print('--------end--------')
# endregion

# 5.使用 map 方法批量提交任务(注意：map方法是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的)
# def work(n):
#     print(f'work is doing task{n}......{os.getpid()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'this is task result of {n}'
#
# if __name__ == '__main__':
#     print('--------start--------')
#     # 创建一个进程池执行器
#     executor = ProcessPoolExecutor(3)
#
#     # 通过 map 方法批量提交任务(结果按照提交的顺序来)
#     results = executor.map(work, range(1, 8))   # 严格按照设定顺序执行
#     # 获取 results 生成器中的内容
#     print(list(results))
#
#     executor.shutdown(wait=True)
#     print('--------end--------')


# 使用 with：进程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
def work(n):
    print(f'work is doing task{n}......{os.getpid()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'this is task result of {n}'

if __name__ == '__main__':
    print('--------start--------')
    # 创建一个进程池执行器
    with ProcessPoolExecutor(3) as executor:
        # 通过 map 方法批量提交任务(结果按照提交的顺序来)
        results = executor.map(work, range(1, 8))
        print(list(results))

    print('--------end--------')