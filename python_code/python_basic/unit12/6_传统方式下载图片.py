import requests     # requests 本身不支持协程

def download_picture(url):
    print(f'downloading picture {url}')
    response = requests.get(url)
    print('download success')

    with open(f'imgs/{url[-10:]}', 'wb') as f:
        f.write(response.content)


def main():
    url_list = [
        'https://i0.hdslb.com/bfs/article/f0ec2604387145abb3d0fdc9064b4bed59a045b8.jpg',
        'https://i0.hdslb.com/bfs/article/42d7120ad5bd5c6ef0a603239050f0753b4bf2a7.jpg',
        'https://i0.hdslb.com/bfs/article/ff8fbd1e968d41446b561bcd7ff57b980073dcea.jpg'
    ]

    for url in url_list:
        download_picture(url)

main()