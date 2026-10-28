
names = ['张三', '李四', '王五']          # 可迭代对象
cities = ['北京', '上海', '深圳']         # 可迭代对象
msg1 = 'hello world'                    # 可迭代对象
msg2 = 'hello'                          # 可迭代对象
age1 = 20                                # 不可迭代对象

def test():
    pass

print(hasattr(names, '__iter__'))
print(hasattr(msg1, '__iter__'))
print(hasattr(msg2, '__iter__'))
print(hasattr(age1, '__iter__'))

it = iter(names)
print(it.__next__())
print(it.__next__())

print('---------------手写迭代器-------------')
# 手写迭代器
it = iter(cities)
print(next(it))
print(next(it))
print(next(it))

print('==========实现方式1================')
# 目标：能够调用所有的Person实例
class Person:
    def __init__(self, name, age, gender, district):
        self.name = name
        self.age = age
        self.gender = gender
        self.district = district

    def __iter__(self):
        return PersonIterator(self)

class PersonIterator:
    def __init__(self, person):
        self.person = person
        # 设置迭代器的初始化状态(指针位置)
        self.index = 0
        # 配置要遍历的内容
        self.attrs = [person.name, person.age, person.gender, person.district]

    # 迭代器的__iter__方法会返回迭代器自身
    def __iter__(self):
        return self

    # 每次调用__next__方法，会根据当前的状态，返回下一个元素
    def __next__(self):
        if self.index >= len(self.attrs):
            raise StopIteration

        # 获取要返回的内容
        value = self.attrs[self.index]
        # 更新迭代器指针的位置
        self.index += 1
        return value


# 目标
p1 = Person('张三', 18, 'male', 'Beijing')
for item in p1:
    print(item)
