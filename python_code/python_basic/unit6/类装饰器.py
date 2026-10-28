"""
类装饰器
1. 包含__call__方法的类，就是类装饰器。
2. 像调用函数一样，去调用类装饰器的实例对象，就会触发__call__方法的调用。
3. __call__方法通常接收一个函数作为参数，并且会返回一个新函数。
"""

class SayHello:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('this is a add function ')
            return func(*args, **kwargs)
        return wrapper

@SayHello()
def add(a, b):
    print(f"{a} + {b} = {a+b}")
    return a + b


result = add(1, 2)
print(result)


print('------带参数的装饰器------')

class SayHello2:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'this is a {self.msg} function ')
            return func(*args, **kwargs)
        return wrapper

@SayHello2('add')
def add2(a, b):
    print(f"{a} + {b} = {a+b}")
    return a + b


result2 = add2(3, 2)
print(result2)


print('-----------多个类修饰器的使用----------')
class Test1:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('这是Test1追加的逻辑 ')
            return func(*args, **kwargs)
        return wrapper

class Test2:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('这是Test2增加的逻辑')
            return func(*args, **kwargs)
        return wrapper

@Test1()
@Test2()
def add3(a, b):
    print(f"{a} + {b} = {a+b}")
    return a + b

result3 = add3(3, 4)
print(result3)