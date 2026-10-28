'''
1. 生成器函数:函数体中如果出现了 yield 关键字，那该函数是「生成器函数」。
2. 生成器对象：调用「生成器函数」时，其函数体不会立刻执行，而是返回一个「生成器对象」。
> 备注：不管能否执行到yield所在的位置，只要函数中有yield关键字，那该函数，就是「生成器函数」。
'''


# def demo1():
#     print('demo函数开始执行了')
#     print(100)
#     if 1 == 0:
#         yield
#     a = 200
#     print(a)
#
# d1 = demo1()

# 生成器对象是一种特殊的迭代器
# region
# def demo2():
#     print('demo2 function is working')
#     print(100)
#     yield 'this is the first data'                  # 暂停执行
#     a = 200
#     print(a)
#     yield 'this is the second data'                  # 暂停执行
#     b = 300
#     print(b)
#     return 'hello world'
#
# d2 = demo2()

# result1 = next(d2)
# print(result1)
#
# result2 = next(d2)
# print(result2)
#
# result3 = next(d2)
# print(result3)

# 本质迭代器，可以直接用for全部遍历
# for item in d2:
#     print(item)

# for 循环背后的逻辑
# gen = iter(d2)
# while True:
#     try:
#         val = next(gen)
#         print(val)
#     except StopIteration:
#         break

# endregion

# yield 也能写在循环里
# region
# def create_car(total):
#     for index in range(total):
#         yield index
#
# indexs = create_car(10)
# for item in indexs:
#     print(item)
# endregion

# yield from 能把一个可迭代对象里的东西依次 yield 出去。(替代：for + yield)
# region
# def demo3():
#     nums = [10, 20, 30, 40, 50]
#     yield from nums
#
# d = demo3()
# r1 = next(d)
# print(r1)
# r2 = next(d)
# print(r2)
# r3 = next(d)
# print(r3)
#
# for i in d:
#     print(i)
# endregion

# 使用：生成器.send(value)可以让生成器继续执行的同时，给上一次yield传值
def demo():
    print('let us go')
    print(100)
    a = yield 'this is the first item'
    print(a)
    b = yield 'this is the second item'
    print(b)
    return 'hello world'

d = demo()
r1 = d.send(None)
print(r1)
r2 = d.send(666)
print(r2)
