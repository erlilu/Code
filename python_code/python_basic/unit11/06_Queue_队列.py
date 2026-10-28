import time
from multiprocessing import Process, Queue

def test(q):
    time.sleep(3)
    result = q.get()
    print(f'i will put one element that is :{result}')


if __name__ == '__main__':
    q = Queue(2)
    q.put('first_element')
    q.put('second_element')
    print(f'queue is full ----{q.full()}')

    p1 = Process(target=test, args=(q,))
    p1.start()

    print('adding a new element in the fulled queue.....')
    q.put('new_element')   # 注意：这里会阻塞，直到子进程取走一个元素

    print('elements of queue is :')
    print(q.get())
    print(q.get())
    p1.join()              # 等待子进程结束