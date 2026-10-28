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
    # 调用三次work函数，分别得到三个协程对象
    coroutine1 = work(1, 2)
    coroutine2 = work(2, 2)
    coroutine3 = work(3, 2)

    # 此处会等待coroutine1执行完成
    res1 = await coroutine1
    print(res1)
    # 此处会等待coroutine1执行完成后，再等待coroutine2完成
    res2 = await coroutine2
    print(res2)
    # 此处会等待coroutine1执行完成后，再等待coroutine2完成，最后在等待coroutine3完成
    res3 = await coroutine3
    print(res3)

    print(time.time() - start)
    print('-------end--------')
    return f'result of main'


# 将协程对象交给事件循环
result = asyncio.run(main())
print(result)
