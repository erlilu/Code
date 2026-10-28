import os
import time
from threading import get_native_id, Thread, RLock

class SpeakThread(Thread):
    def __init__(self, lock, **kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(5):
            with self.lock:
                print(f'i am speaking{index}, pid is {os.getpid()}, thread id:{get_native_id()}')
            time.sleep(1)

class StudyThread(Thread):
    def __init__(self, lock, **kwargs):
            super().__init__(**kwargs)
            self.lock = lock

    def run(self):
        for index in range(5):
            with self.lock:
                print(f'i am studying {index}, pid of process is: {os.getpid()}, thread id:{get_native_id()}')
            time.sleep(1)


if __name__ == '__main__':
    print(f'-----------start-----------process pid是：{os.getpid()}, thread id:{get_native_id()}')
    lock = RLock()
    t1 = SpeakThread(lock)
    t2 = StudyThread(lock)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('-----------end-----------')

