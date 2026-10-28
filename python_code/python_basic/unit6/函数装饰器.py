
# 手动修饰【不推荐】
def say_hello(func):
    def wrapper(a, b):
        print('this is a add')
        return func(a, b)
    return wrapper

def add(x, y):
    res = x + y
    print(f'{x} + {y} = {res}')
    return res


add_pro = say_hello(add)
result = add_pro(10, 20)
print(result)


"""
关键点：
1. 接收器修饰的函数、同时返回新函数（wrapper）。
2. 修饰器“吐出来”的是wrapper函数，以后别人调用的也是wrapper函数。
3. 为了保证参数的兼容性，wrapper函数要通过 *arg和 **kwargs 接收参数。
4. wrapper 函数中主要做的是：调用原函数（被修饰的函数）、执行其他逻辑，但要记得将原函数的返回值 return 出去。
"""



# @修饰器名 【推荐】
def say_hello2(func):
    def wrapper(*args, **kwargs):
        print('this is a add')
        return func(*args, **kwargs)
    return wrapper

@say_hello2                 # 相当于 add2 = say_hello2(add)
def add2(x, y):
    res = x + y
    print(f'{x} + {y} = {res}')
    return res


result2 = add2(10, 20)
print(result2)