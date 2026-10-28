import asyncio


# 情况一：包含I/O操作
async def work():
    print('work start⬇️')
    print('work doing......')
    # 官方内置 asyncio.sleep ，模拟I/O
    res = await asyncio.sleep(3)
    print(res)
    print('work end⬆️')
    return 'result of work'

async def main():
    print('---------start-----------')
    # await 去等待一个协程对象
    res = await work()
    print(res)
    print('---------end-----------')
    return 'result of main'

result = asyncio.run(main())
print(result)



# 情况二：不包含任何的I/O操作
# region
# async def work():
#     print('work start⬇️')
#     print('work doing......')
#     print('work end⬆️')
#     return 'result of work'
#
#
# async def main():
#     print('---------start-----------')
#     # await 去等待一个协程对象
#     res = await work()
#     print(res)
#     print('---------end-----------')
#     return 'result of main'
#
# result = asyncio.run(main())
# print(result)
# endregion
