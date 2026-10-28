from time import sleepfrom abc import abstractmethodfrom abc import ABC

# 第七章 类

# 一、属性、类、object类、抽象类
```python
class Person:
   # 类属性
    max_age = 120
    plant = 'earth'
    def __init__(self, name, age, gender):
        self.name = name        # 公有属性
        self._age = age          # 受保护的属性
        self.__gender = gender    # 私有属性
```
## 类的初始化 
1. 初始化方法：给当前正在创建的实例对象添加属性。
2. 初始化方法收到的参数：当前正在创建的实例对象self、其他的自定义参数。
3. 编写代码创建Person类实例的时候，python会自动调用init。

## 创建实例、实例属性、类属性
1. 实例属性只能通过实例访问，不能通过类访问。
2. 类属性：可以通过类访问，也可以通过实例访问。

## 三种权限
1. 公有属性：当前类中、子类中、类外部，都可以访问。【】
2. 受保护的属性：当前类中、子类中，都可以访问。【_】
3. 私有属性：仅能在当前类中访问。【__】(python底层通过重命名的方式，实现私有属性的)
## 抽象类
1. 定义：是一种不能直接实例化的类，通常作为“规范”，让子类继承，并实现其中定义的【抽象方法】。
2. @abstractmethod，如果类继承了ABC类，那么此类必须为抽象类。

```python
from abc import ABC, abstractmethod

class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass

class Person(MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def run(self):
       print(f'my name is {self.name},{self.age} running!')

```
# 二、方法

```python
from datetime import datetime


class Person:
   max_age = 120
   planet = 'earth'

   def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender

   # 自定义方法
   def speak(self, msg):
      print(f'I want to say {msg}')

   def run(self, distance):
      print(f'{self.name} can run {distance} m')

   # 定义类方法
   @classmethod
   def class_function1(cls):
      print('I am a class method')

   @classmethod
   def change_planet(cls, value):
      cls.planet = value

   @classmethod
   def create(cls, info_str):
      # 从info_str中获取到有效信息
      name, year, gender = info_str.split('-')
      # 获取当前年份
      current_year = datetime.now().year
      # 计算年龄
      age = current_year - int(year)
      # 必须返回创建的Person类的实例对象
      return cls(name, age, gender)
   
   
   @staticmethod
   def is_adult(year):
      age = datetime.now().year - year
      return age >= 18


p3 = Person.create('李华-2002-女')
print(p3.__dict__)          # {'name':'李华', 'age':24, 'gender':'女'}
```
## 自定义方法、实例方法、类方法、静态方法、常用方法、getter与setter、魔法方法
1. 执行**自定义方法**的顺序： 实例对象自身p1 ==> 实例的“缔造者”的身上【class】。 
2. **实例方法**：供实例调用的方法【给实例添加行为】，通过实例调用p1.方法名()。
3. **类方法**：
   1. @classmethod 装饰器、cls参数。
   2. 因为收到cls参数，类方法可以访问类属性。
   3. 类方法通常实现与类相关的逻辑：例如类级别的信息、一些工厂方法。
4. **静态方法**:保存在类身上
   1. @staticmethod 修饰器。
   2. 静态方法单纯定义在类中，它不会收到：self、cls参数，它收到的参数都是自定义参数。
   3. 内部不会访问任何:类和实例相关的内容。因此，使用类去调用，不建议使用实例。
   4. 用于定义：与类相关的工具方法。
5. 常用方法：
   1. isinstance(instance, Class),作用：判断某个对象是否为指定类或其子类的实例。【返回bool型】
   2. issubclass(Class1, Class2),作用：判断某个类是否是另一个类的子类。【返回bool型】
## getter与setter
1. 通过getter和setter来对属性(受保护属性、私有属性)进行修改。
2. @property: getter方法，当访问Person实例的age属性时，下面的age方法就被自动调用。
3. @属性.setter: setter方法，当修改Person实例的age属性时，下面age方法就会被自动调用。

## 魔法方法：以__XX__名命的特殊方法【下划线开头和结尾】
1. 特点：不需要手动调用，只需要准备好这些放啊，python会在特定场景下自动调用。
2. __str__: 当调用print(对象)或str(对象)时
3. __len__: 当调用len(对象)时
4. __lt__: 当执行对象1 < 对象2时
5. __gt__: 当执行对象1 > 对象2时
6. __eq__: 当值行对象1 = 对象2时
7. __getattr__: 当访问不存在的属性时
```python
class Person:
    def __init__(self, name, age, id_card):
        self.name = name
        self._age = age             # 受保护的属性
        self.__id_card = id_card    # 私有属性
        
    def __str__(self):
        return f'{self.name}-{self.age}'

    # 注册age属性getter方法，当访问Person实例的age属性时，下面的age方法就被自动调用
    @property
    def age(self):
        return self._age

    # 注册age属性setter方法，当修改Person实例的age属性时，下面age方法就会被自动调用
    @age.setter
    def age(self, value):
        if value <= 120:
            self._age = value
        else:
            print('age is ill')
```
# 三、继承、方法重写、多重继承
1. 继承
   1. 定义子类
   2. 子类中，两种放视调用父类初试化，来继承属性。【推荐法1】
2. 重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会覆盖父类的方法。
   1. 同样可以使用super来使用父类的同名方法。
3. 多重继承：只能用类名来继承初始化
   1. 类的_mro_属性：用于记录属性和方法的查找顺序。
```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def speak(self, msg):
      print(f'I want to say {msg}')
        
class Worker:
    def __init__(self, company):
      self.company = company
    
    def work(self):
        print(f'在{self.company}打螺丝')    

class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 方法1,更推荐
        super().__init__(name, age, gender)    
        # 方法2
        # Person.__init__(self, name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

    def speak(self, msg):
        super().speak(msg)
        print(f'I am a student, I want to say:{msg}')

# 多重继承，只能用类名来继承初始化
class Child(Person, Worker):
    def __init__(self, name, age, gender, company, child_id):
        Person.__init__(self, name, age, gender)
        Worker.__init__(self, company)
        self.child_id = child_id

    def eat(self):
        print('我要喝奶奶')
```
# 四、多态【标准多态、鸭子多态】
1. 标准多态
   1. 概念：同一个方法名，在不同的对象上调用时，能呈现出不同的行为。
   2. 三要点： 必须继承父类，子类的方法必须为重写、最后必须类型注解【继承、重写、类型注解】
2. 鸭子多态
   1. 不需要向上继承父类，只要不同类中的方法一致即可【假重写】(不需要继承、不需要类型注解)
```python
class Animal:
    def speak(self):
        print('发出动物的叫声')

class Dog(Animal):
    def speak(self):
        print('汪汪汪！')

class Cat(Animal):
    def speak(self):
        print('喵喵喵！')

def make_sound(animal: Animal):
    animal.speak()
```
-----------

# 模块
## 模块入门+自定义模块
### __all__
- 在python模块中，可以通过 __all__来控制【from 模块 import *】能导入哪些内容。
- __all__的值可以时：列表、元组。

### __name__ 
- __name__是每个Python模块(.py文件)都拥有的一个内置变量。
- 它的具体值取决于模块的运行方式：
  - 作为主程序直接运行，__name__的值是__mian__.
  - 作为模块被导入到其他程序中运行，__name__的模块的文件名(不带.py)
测试代码
```python
if __name__ == '__main__':
    pass
```

## 标准库模块
- import copy : 拷贝对象--深拷贝、浅拷贝。
- import os : 操作系统相关文件--文件、文件夹、路径系统层面的操作。
- import random : 随机数相关--生成随机数、随机选择、洗牌。
- import time : 时间相关操作--获取时间、延时、格式化时间等。
- import math : 数学相关--开平方、去绝对值等等。
- import sys : Python 解释器相关操作

## 包package
1. 在python中，包含__init__.py的文件夹就是一个包（package）。
2. 包与模块的关系
   1. 一个模块就是一个.py文件，包是用来管理模块的目录
   2. 一个包有多个模块，也可以有多个子包。
3. 可以通过创建---新建->Python软件包,来创建。
4. 关于 __init__.p 文件：
   1. __init__.py 是包的初始化文件，在包被导入时，__init_.py 会被自动调用。
   2. __init__.py 中可以编写一些包的初始化逻辑。
   3. __init__.py 中所定义的内容，会被【from 包名 import *】形式全部引入。
   4. __init__.py 中也可以使用 __all__ 来控制包中的哪些模块可以被【from 包名 import *】引入。