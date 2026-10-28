import time
from multiprocessing import Process, Pipe

def test1(con1):
    data = con1.recv()
    print(f'test2 received {data}')

def test2(con2):
    time.sleep(2)
    con2.send(100)
    print('test1 sent 100')


if __name__ == '__main__':
    # 单向时：con1为只能接收，con2为只能发送。【先接收，再发送】
    con1, con2 = Pipe(duplex=False)

    p1 = Process(target=test1, args=(con1,))
    p2 = Process(target=test2, args=(con2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
