import asyncio
import aiohttp
from pathlib import Path


async def download_picture(session, url, save_dir):
    """下载单张图片"""
    print(f'开始下载: {url}')

    # 用 async with 管理响应，自动释放连接
    async with session.get(url) as response:
        if response.status != 200:
            print(f'下载失败，状态码 {response.status}: {url}')
            return
        content = await response.read()

    # 从 url 提取文件名
    filename = url.split('/')[-1] or url[-10:]
    filepath = save_dir / filename

    # 写入本地文件
    with open(filepath, 'wb') as f:
        f.write(content)

    print(f'下载成功: {filepath.name}')


async def main():
    url_list = [
        'https://i0.hdslb.com/bfs/article/f0ec2604387145abb3d0fdc9064b4bed59a045b8.jpg',
        'https://i0.hdslb.com/bfs/article/42d7120ad5bd5c6ef0a603239050f0753b4bf2a7.jpg',
        'https://i0.hdslb.com/bfs/article/ff8fbd1e968d41446b561bcd7ff57b980073dcea.jpg'
    ]

    # 1. 确保 imgs 文件夹存在（相对脚本所在目录）
    save_dir = Path(__file__).parent / 'imgs'
    save_dir.mkdir(exist_ok=True)

    # 2. 用 async with 管理 session，无论是否异常都自动关闭
    async with aiohttp.ClientSession() as session:
        # 3. 创建协程列表
        tasks = [download_picture(session, url, save_dir) for url in url_list]
        # 4. 并发执行，return_exceptions=True 避免一个失败全部中断
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())