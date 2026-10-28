import asyncio

# 定义一个协程函数
async def work():
    print('work start⬇️')
    print('work doing......')
    print('work end⬆️')
    return 'result of work'

# 调用协程函数，会得到协程对象
coroutine_object = work()

# asyncio.run() 做了三件事：
# 1.创建一个时间循环。
# 2.将收到的协程对象，包装成一个任务task，交给时间循环。
# 3.启动时间循环。
# 注意：asyncio.run 会阻塞当前线程，直到任务执行完毕，并返回该任务 return 的最终结果。
result = asyncio.run(coroutine_object)
print(result)
