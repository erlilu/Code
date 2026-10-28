import asyncio
import aiohttp

"""
Python 环境缺少有效的 SSL 根证书，无法验证 i0.hdslb.com 的证书颁发机构

import ssl

ssl_context = ssl.create_default_context(cafile=certifi.where())
async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
    # ... 你的下载逻辑
"""

async def download_picture(session, url):
    print(f'downloading picture {url}')
    # 发送网络请求，获取这张图片【请求发出去后，要等待服务器把数据返回，等的这段时间就是I/O等待】
    response = await session.get(url)
    # 等待数据【图片数据可能分多次传输，需要等待数据全部读完，等的这段时间也是I/O等待】
    content = await response.read()

    # async with session.get(url) as response:
    #     content = await response.read()
    # print('download success')

    with open(f'imgs/{url[-10:]}', 'wb') as f:
        f.write(content)

    # 释放链接资源【告诉 aihttp，此链接不再使用，可以回收】
    await response.release()


async def main():
    url_list = [
        'https://i0.hdslb.com/bfs/article/f0ec2604387145abb3d0fdc9064b4bed59a045b8.jpg',
        'https://i0.hdslb.com/bfs/article/42d7120ad5bd5c6ef0a603239050f0753b4bf2a7.jpg',
        'https://i0.hdslb.com/bfs/article/ff8fbd1e968d41446b561bcd7ff57b980073dcea.jpg'
    ]

    # 创建一个会话对象（发请求的工具）
    session = aiohttp.ClientSession()
    try:
        # 创建多个多协程对象
        coroutine_list = [download_picture(session,url) for url in url_list]
        # 将多个协程对象交给事件循环
        await asyncio.gather(*coroutine_list)
    finally:
        # 关闭回话
        await session.close()         # I/O操作，前面+ await

    # # 用 async with 管理 session，自动关闭
    # async with aiohttp.ClientSession() as session:
    #     coroutine_list = [download_picture(session, url) for url in url_list]
    #     await asyncio.gather(*coroutine_list)

asyncio.run(main())


