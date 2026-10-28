from unit9.文件操作 import resultfrom unit6.数据容器 import score_listfrom unit9.文件操作 import resultfrom cgitb import resetfrom unit9.文件操作 import resultfrom unit9.文件操作 import resultfrom unit9.文件操作 import resultfrom idlelib import rpc

# 第五章 函数[含高阶]

# 基本使用
## 1. 定义, 参数（位置参数、关键字参数）
```python
def func1(a, b):
    print("this is a function")
    print(a+b)
```
## 2. 函数·限制传参方式
具体规则：
1. / **前面**只能用位置参数，* **后面**只能用关键字参数
2. /和*同时使用时，/必须在*前面
```python
def greet(name, /, gender, *, age, height):
    print(f'my name is {name}, gender is {gender}, {age} years old, {height}cm')

greet('ming', 'male', age=18, height=172)
greet('ming', gender='male', age=18, height=172)
```
## 3. 参数默认值
规则：
1. 默认参数必须在必选参数后面。换言之，某个形参一旦设置了默认参数，后面的所有参数也必须设置为默认参数
2. print()函数，系统中的默认参数值为end=\n
```python
def greet(name, gender, age, height, msg='hello'):
    print(f'my name is {name}, gender is {gender}, {age} years old, {height}cm')

greet('ming', 'male', age=18, height=172)
greet('ming', gender='male', age=18, height=172, msg='hi')
```
------
# 重新认识函数
##  1. 可变参数、多返回值_参数的打包与解包
1. 可变位置参数: 定义函数时，在形参名前加*，可以接受任意数量的位置参数，并打包成一个**元组**。 
   1. args只是形参名，可以随意更改; 
   2. args存放的是，函数调用时，所传入的所有位置实参； 
   3. args的数据类型是元组
2. 可变关键字参数：在形参名前加**，可以接受任意数量的关键字参数，并打包成一个**字典**。
   1. kwargs只是一个形参名，可以任意更改
   2. kwargs存放的是，函数调用时，所传入的所有参数关键字实参
   3. kwargs的数据类型是字典
3. 可变位置参数、可变关键字参数，也能与其他类型的参数一起使用。
```python
def test1(*argss):
    print(argss)
test1('ming', 'male', 18, 172)
# ('ming', 'male', 18, 172)
def test2(**kwargs):
    print(kwargs)
test2(name='ming', gender='male', age=18, height=172)
# {name='ming', gender='male', age=18, height=172}
def test3(*args, **kwargs):
    print(args)
    print(kwargs)
test3('ming', 'male',age=18, height=172)
# ('ming', 'male')
# {age=18, height=172}
```
### 打包接收参数
1. *args：打包所有的未知参数
2. **kwargs：打包所有的关键字参数
### 解包传递参数
1. *变量名：将元组拆解为一个一个独立的位置参数
2. **变量名：将字典拆解为一个一个key=value形式的关键字参数
```python
def show_info(num1, num2, num3, name, age, gender):
    print(num1, num2, num3)
    print(name, age, gender)

nums = (10, 20, 30)
person = {'name': '张三', 'age': 18, 'gender': '男'}
show_info(*nums, **person)
```
### 打包接收参数 和 解包传递参数 一起使用
```python
def show_info(*args, **kwargs):
    print(args)
    print(kwargs)

nums = (10, 20, 30)
person = {'name': '张三', 'age': 18, 'gender': '男'}
show_info(*nums, **person)
```
## 2. 高阶函数、匿名函数、数据处理函数、常用内置函数
### 高阶函数
1. 定义：当一个函数的「参数是函数」或者「返回值是函数」，那该函数就是高阶函数。
2. 意义：复用性高、更灵活、是修饰器和闭包的基础
```python
def info(msg):
    return 'tips:' + msg

def warn(msg):
    return 'warn:' + msg

def error(msg):
    return 'error:' + msg

def log(func, text):
    print(func(text))

log(info, '文件保存成功')
log(warn, '磁盘空间不足')
log(error, '该用户不存在')
```

### 匿名函数lambda
1. 定义：没有名字的函数，无需使用def关键字去定义；
2. 使用lambda关键字来定义；格式----- lambda 参数：表达式
3. 使用场景：函数只用一次，只做一点小事
```python
add = lambda x, y : x + y

is_adult = lambda age: '成年' if age > 18 else '未成年'
```

### 其他常见数据处理函数：map(), filter(), sorted(), reduce()
#### map()
1. map函数：对一组数据中的每个元素，统一执行某种操作(加工)，并生成一组新数据。
2. 语法格式：map(操作函数，可迭代对象)。
3. 统一数据处理，map函数的返回值是一个迭代器对象，需要手动遍历，或者手动类型转换。
4. 注意点：
   1. 延迟执行：map不会立刻计算，只有在：“需要结果”时才执行计算。
   2. 返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”。
   3. map不会影响元素数量
```python
# 字符串转化
names = ('python', 'java', 'js')
result = map(lambda x : x.upper(), names)
print(tuple(result))            # (PYTHON, JAVA, JS)

# 类型转换
str_name = {'1', '2', '3'}
result = map(int, str_name)
print(set(result))          # 1,2,3
```
#### filter()
1. 从一组数据中，筛选出符合条件的元素(过滤)，并组成一组新数据。
2. 语法格式：filter(过滤函数，可迭代对象)
3. 注意点：
   1. 延迟执行：filter不会立刻筛选，只有在“需要结果”时才执行。
   2. 返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”。
   3. filter不会影响元素数量。
```python
# 筛选数值
nums = [10, 20, 30, 40, 50]
result = filter(lambda n: n > 30, nums)
print(list(result))  # [40, 50]
print(nums)  # [10, 20, 30, 40, 50]

persons = [
   {'name': '张三', 'age': 15, 'gender': '男'},
   {'name': '李四', 'age': 16, 'gender': '女'},
   {'name': '王五', 'age': 18, 'gender': '男'},
   {'name': '李华', 'age': 20, 'gender': '女'},
]
result = filter(lambda p: p['age'] >= 18, persons)
print(list(result))

# filter函数的特殊用法：如果不传递过滤函数，那么自动会过滤掉‘假值’
data = [0, 1, '', 'hello', [], (), 5]
result = filter(None, data)
print(list(result))
```
#### sorted()
1. 对一组数据进行排序，返回一组新数据。
2. 语法格式：sorted(可迭代对象， key=xxx, reverse=xxx)
```python
nums = [30, 40, 20, 10]
result = sorted(nums, reverse=True)
print(result)           # [10, 20, 30, 40]

# 按照字符串的长度排序
names = ['python', 'sql', 'java']
result = sorted(names, key=lambda n: len(n))
print(result)
```
#### reduce()
1. 将一组数据不断“合并”，最周归并成一个结果。
2. 语法格式：reduce(合并函数，可迭代对象，初始值)。
3. 备注：reduce函数需要从 functools 模块中引入才能使用。
```python
from functools import reduce
# 数值统计
nums = [1, 2, 3, 4, 5]
result = reduce(lambda a,b : a + b, nums, 10)       # 两两依次累加
print(result)               # 25    【10 + 15】
```
## 3. 函数表达式、列表推导式
### 函数表达式
'result1' if 条件 else 'result2'
### 列表推导式
1. 用一条简洁语句，从可迭代对象中，生成新列表的语法结构
2. 备注：列表推导式本质上是对 for循环 + append() 的一种简写形式。
3. 语法格式：[表达式 for 变量 in 可迭代对象]
```python
# 输出2倍的n
nums = [10, 20, 30, 40]
# 方法一：
result1 = list(map(lambda n: 2*n, nums))

# 方法二：
result2 = [n * 2 for n in nums]

# 带条件的列表推导式
result3 = [n * 2 for n in nums if n > 20]
```
### 字典、集合推导式
```python
names = ['张三', '李四', '王五']
scores = [60, 70, 80]
result1 = {names[i]: scores[i] for i in range(len(names))}

result2 = {n + '!' for n in names}

# 没有元组推导式
```
## 4. 浅拷贝<——>深拷贝
### 浅拷贝
1. 创建一个新的外层容器，但内部元素仍然引用原来的对象。
2. 存在问题：嵌套数据仍然是共享的，修改嵌套数据会相互影响。

### 深拷贝
> 比较消耗性能
1. 创建一个新的外层容器，对其内部所有的【可变子对象】进行递归复制
   - 备注：
     - 深拷贝可以彻底消除数据之间的相互影响。
     - 深拷贝遇到【不可变对象】不会复制，会直接引用。【例如：元组】
   - 注意点：
     - 深拷贝致富只可变对象，不可变对象会直接引用。

```python
import copy
# 浅拷贝
nums1 = [10, 20, 30, 40]
nums2 = copy.copy(nums1)
nums2[3] = 99

nums3 = [10, 20, 30, [40, 50]]
nums4 = copy.copy(nums3)        # 嵌套数据会相互影响


# 深拷贝
nums5 = copy.deepcopy(nums3)
nums5[3][0] = 99                # 嵌套数据不会受到影响
```
## 5. 四种作用域
1. 内建作用域Built-in
2. 全局作用域Global「关键字：global」
3. 外层函数作用域Enclosing【别名：闭包作用域】 「nonlocal」
4. 局部作用域Local

## 6. 闭包
1. 前置知识1
   - 每次调用函数时，python都会为函数创建一个新的局部作用域
   - 函数执行完毕后，这个局部作用域会被销毁，其中的局部变量也会随之被释放
2. 前置知识2
   - 在python中，内层函数可以访问其外层函数作用域中的变量
   - 访问外层函数变量无需使用nonlocal；但是修改外层变量需要使用nonlocal
代码参考----[[闭包.py]]

3. 注意点
   1. 调用n次外层函数，就会得到n个不同的闭包，并且这些闭包之间互不影响。
   2. 内层函数中用到的外层变量是可变对象，多个闭包之间依然互不影响。

4. 闭包的优点：
   1. 可以记住状态：不用全局变量，也不用写类，就能在多次调用之间保存数据。
   2. 可以做配置过的函数：先传一部分参数，把环境固定住，得到一个定制版函数。
   3. 可以实现简单的数据隐藏：外层变量对外不可见，只能通过内层函数访问。
   4. 是装饰器(decorate)等高级用法的基础。

5. 闭包的缺点
   1. 理解成本较高：对初学者不太友好，滥用会让代码难读。
   2. 如果闭包里引用了很大的对象，又长期不释放，可能会增加内存占用。
   3. 很多场景下，其实【类 + 实例属性】会更清晰，闭包不一定是最优解。

## 7.装饰器
### 函数装饰器
1. 基本内容
   1. 装饰器是一种【可调用对象】（通常是函数），它能接受一个函数作为参数，并且会返回一个新函数。
   2. 装饰器可以在不修改原函数代码的前提下，增强或改变原函数的功能。
2. 关键点：
   1. 接收器修饰的函数、同时返回新函数（wrapper）。
   2. 修饰器“吐出来”的是wrapper函数，以后别人调用的也是wrapper函数。
   3. 为了保证参数的兼容性，wrapper函数要通过 *arg和 **kwargs 接收参数。
   4. wrapper 函数中主要做的是：调用原函数（被修饰的函数）、执行其他逻辑，但要记得将原函数的返回值 return 出去。

### 类装饰器
类装饰器
1. 包含__call__方法的类，就是类装饰器。
2. 像调用函数一样，去调用类装饰器的实例对象，就会触发__call__方法的调用。
3. __call__方法通常接收一个函数作为参数，并且会返回一个新函数。

## 8.类型注解
> leetcode 中，示例代码均带有注解
1. 变量类型注解
   1. 格式---- 【参数: 类型名】
   2. 参数有多种变量时，注意区分python的版本，3.10+才是新版本简单写法
2. 函数类型注解
   1. 格式---- 【函数名(参数1: 类型， 参数2:类型) -> 返回值类型:】
