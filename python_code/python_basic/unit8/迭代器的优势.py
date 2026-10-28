"""
1. 迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用。
2. 当数据量很大，不确定用多少结果时，推荐使用迭代器。
【不会挤爆内存】
"""

class Fibo:
    def __init__(self, total):
        self.total = total
        self.index = 0

        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.total:
            raise StopIteration

        # fibo逻辑
        if self.index < 2:
            value = 1
        else:
            value = self.pre + self.cur
            self.pre, self.cur = self.cur, value

        self.index += 1
        return value

f1 = Fibo(10)
for item in f1:
    print(item)
