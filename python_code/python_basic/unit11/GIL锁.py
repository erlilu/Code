# Rlock示例1: 让打印是完整的
from threading import Thread, RLock


def show_info1(lock):
    for index in range(10):
        with lock:
            print('ming', end='')
            print('jing', end='')
            print('cheng',)

def show_info2(lock):
    for index in range(10):
        with lock:
            print('Jethro', end='')
            print('Ming',)


if __name__ == '__main__':

    lock = RLock()
    t1 = Thread(target=show_info1, args=(lock, ))
    t2 = Thread(target=show_info2, args=(lock, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
