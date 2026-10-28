import asyncio
import time


# 定义一个协程函数
async def work(n, delay):
    print(f'work {n} start')
    # 模拟一个I/O等待
    await asyncio.sleep(delay)
    print(f'work {n} end')
    return f'result of work is:{n}'

async def main():
    print('------start-------')
    start = time.time()
    # asyncio.creat_task() 会把一个协程对象包装成一个可被事件循环调度的任务，并注册到时间循环中
    # 包装成任务---> 放入事件循环
    task1 = asyncio.create_task(work(1, 2))
    task2 = asyncio.create_task(work(2, 2))
    task3 = asyncio.create_task(work(3, 2))

    res1 = await task1
    print(res1)
    res2 = await task2
    print(res2)
    res3 = await task3
    print(res3)

    print(time.time() - start)
    print('-------end--------')
    return f'result of main'


# 将协程对象交给事件循环
result = asyncio.run(main())
print(result)

"""
1. 执行之后，瞬间按照顺序完成 work {n} start
2. 三个I/O任务被asyncio.create_task() 挂起
3. 等待I/O 等2s结束
4. 执行 work {n} end
5. 最后一次打印res，得到返回值。任务完成✅
"""