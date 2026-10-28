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

    # 把多个协程对象同时丢给事件循环，并在全部执行完成后，一次性拿到去全部的结果。
    res = await asyncio.gather(
        work(1,2), work(2,2), work(3,2)
    )
    print(res)
    print(time.time() - start)
    print('-------end--------')
    return f'result of main'


# 将协程对象交给事件循环
result = asyncio.run(main())
print(result)
