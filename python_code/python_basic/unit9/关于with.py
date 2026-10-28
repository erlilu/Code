
# 定义一个 Person 类，让其实例对象遵循：上下文管理器协议
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print('i am studying')

    def __enter__(self):
        print('------i am a enter magical function-------')
        # __enter__方法：with 中的代码执行【之前】调用，其返回值会赋值给 as 后的变量.
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('------i am a exit magical function--------')
        # exc_type  ：异常类型
        # exc_val   ：异常对象
        # exc_tb    ：异常追踪信息
        print(f'{exc_type}')
        print(f'{exc_val}')
        print(f'{exc_tb}')
        return True

# p1 = Person('张三', 18)
# p1.study()

with Person('李四',20) as p1:
    p1.study()
    # p1.speak()
    print(777)