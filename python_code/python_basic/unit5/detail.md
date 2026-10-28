from unittest import resultfrom math import expm1from unittest import resultfrom unittest import resultfrom pickletools import read_long4from unittest import resultfrom datetime import datefrom unittest import resultfrom socket import socket

# 第六章 数据容器
# 0、数据容器通用的方法
1. sort(数据容器, reverse=布尔值)：对容器排序(从小到大，不会改变原容器)reverse用于控制排序方式，返回值：经过排序的新容器
2. len(数据容器)：获取容器中元素的个数，返回值：元素个数。
3. max(数据容器)：返回容器中或多个值中的最大值，返回值：最大值。
4. min(数据容器)：返回容器中或多个值中的最小值，返回值：最小值。
5. sum(数据容器)：对容器中所有元素求和(只能是数值类型)，返回值：所有元素的和。【注意：字符串不能使用数值类型】

# 1、列表 list、[]、【增删改查】
## 下标
1. 正索引：从**左往右**数，起始元素是0，随后是1，依次类推。
2. 负索引：从右往左数，起始元素是-1，随后是-2，一次类推。
3. 嵌套列表
```python
nums = [10, 20, ['hello', 'hi'], 40, 50]
print(nums[2][1]) # hi
```
## 增删改查
1. 增加
   1. .append(): 在列表尾部追加一个元素
   2. .insert(index, segment) : 在列表指定下标添加一个元素
   3. .extend(可迭代对象): 将可迭代对象中的内容依次取出，追加到列表尾部。【字符串会被拆分为单个字符】
2. 删除
   1. .pop(index):删除指定位置的元素，并将删除的元素返回。
   2. .remove(value):删除列表中第一次出现的指定值。
   3. .clear():删除列表中的所有元素(变成一个空列表)。
   4. del 列表[indx]删除指定位置的元素。
3. 修改
   1. 列表[index] = value ：通过下标修改指定位置的元素
4. 查找
   1. 列表[index]:通过下标获取指定位置的元素。
5. 列表的常用方法
   1. 列表.index(value): 查找指定元素在列表中第一次出现的下标，返回值：元素下标。
   2. 列表.count(value): 统计某个元素在列表中出现的次数，返回值：元素出现的次数。
   3. 列表.reverse(): 反转列表，无需参数，返回值：无。
   4. 列表.sort(reverse=bool):对列表排序（从小到大，会改变原列表—），返回 值：无。
6. 列表的循环遍历。遍历：把容器中的元素依次取出，并对它们进行处理的过程。 while、for
```python
# while 循环遍历
score_list = [54, 54, 23, 76, 68, 90]

index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1
```

```python
# for 循环遍历
score_list = [54, 54, 23, 76, 68, 90]
n = 5
# 写法一
for item in score_list:
   print(item)
# 写法二
for index in range(len(score_list)):
   print(score_list[index])
# 写法三
for index, item in enumerate(score_list, start=n):  # 默认为0
    print(index, item, score_list[0]) 
```
# 2. 元组tuple、()、【查】
元组是一种和列表类型的数据容器，他和列表的区别是：元组中的元素不可修改。但元组中如果存放了可变类型(列表)，那可变类型中的内容仍可以修改。
1. 定义元组,()或者tuple()
2. 定义只有一个元素的元组，需要加“,”
3. 常用方法： 
   1. .index(value):获取指定元素在元组中第一次出现的下标。
   2. .count(value):统计指定元素在元组中出现的次数。
4. 内置函数【除统用外】
   1. .sorted(),对元组进行排序(不修改原元组，返回一个新的列表)
5. **实际开发中的元组，不一定是我们自己定义的，比如函数的可变参数*args就是元组**
```python

# 定义空元组
t1 = ()
t2 = tuple()

# 定义一个只有一个人元素的元组
t3 = ('hello',)
t4 = (18, )

# 5.
def demo(*args):
    return sum(args)
result = demo(100, 200, 300)
print(result) # 600
```

## 函数_解包列表或与元组传参
1. 函数调用时，正常传递：列表 或 元组。
2. 函数调用时，使用*对：列表 或 元组进行解包后，再传递参数。
3. 定义函数---使用*打包
4. 调用函数---使用*解包
```python
list1 = [100, 200, 300, 400]
tuple1 = ('hello', 'hi', 'X')

def test1(data):
    print(f'{data}')

def test2(a, b, c, d):
    print(f'{a}, {b}, {c}, {d}')
    
def test3(*args):
    print(f'{args}')
# 正常传递
test1(list1)
# 使用*对 列表 或 元组 进行解包后，在传递参数
test2(*list1)  # 相当于：test2(100, 200, 300)
test3(*tuple1) # 相当于：test3('hello', 'hi', 'X')
```

# 3. 字符串
1. 数据容器的角度：字符串就是存放多个字符的容器。
2. 【支持】:下标(索引值)
3. 【不支持】：不可修改、不可嵌套
4. 常用方法：
   1. index():获取指定字符在字符串中第一次出现的下标。
   2. split():将字符串按照指定字符进行分隔，并返回一个列表。
   3. repalce():将字符串中的某个字符串片段，替换成目标字符串.
   4. count():统计指定字符在字符串中出现的次数。
   5. strip():从某个字符串中和删除指定字符串中的任意字符。【规则：从字符串两端开始删除，直到遇到第一个不在指定字符串中的字符就停下。】
   6. len():统计字符串中，字符的个数(字符串的长度)
```python
msg1 = 'welcome come to china'
result1 = msg1.index('i')  # 11,【空格也占用下标】

msg2 = 'hello@jethro@world'
result2 = msg2.split('@')
print(result2)  # ['hello', 'jethro', 'world']

result3 = msg1.replace('c', 'C')
print(result3)  # welcome to China

result4 = msg1.count('o')
print(result4)   # 2

sentence1 = '6666句6子666'
sentence2 = '1234句12子4312'
result5 = sentence1.strip('6')
result6 = sentence2.strip('1324')
result57 = len(sentence1)
print(result5)  # 句6子
print(result6)  # 句12子
print(result57) # 10
```

# 4. 序列【列表、元组、字符串都是序列】
> 能连续存放元素的数据容器，元素有先后顺序，切可以通过下标访问。
## 序列的操作
1. 切片：从序列中按照指定范围，取出一部分元素，形成一个新的序列的操作。序列[起始索引:结束索引:步长]
2. 相加：两个同类型的序列才能相加(字符串+字符串、列表+列表、元组+元组)
3. 相乘：将数列进行重复n次。注意：n必须为整数，不能为浮点数。
```python
# 步长为n: 每次跳过n-1位取出
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[0:5:1]    # [10, 20, 30, 40, 50] 【不包含5下标的内容】
list3 = list1[1:8:2]    # [20, 40, 60, 80]
# 默认方式
list4 = list1[::]       # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list5 = list1[:999:]    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list6 = list1[3::]      # [40, 50, 60, 70, 80, 90, 100]
list7 = list1[:5:]      # [10, 20, 30, 40, 50]
# 倒序【当起始索引 大于 结束索引 时，步长必须为负数，否则结果是空列表】
list8 = list1[7:2:-1]   # [80, 70, 60, 50, 40]

# 对元组、字符串的切片同理
```
# 5. 集合、{}、({})
集合特点：【集合是可以去重的数据容器，当只关心元素是否存在，而不在乎顺序时，首选集合】
1. **内部的元素无序(不保证顺序)、不能通过下标访问元素、会自动去除重复元素。**
2. 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】：只有“不可变”的东西，才可以安全放进集合里。
## 可变集合set: 创建后可以增删元素。
## 不可变集合frozenset: 创建后不可以增删元素。
## 【增】
1. .add(item):向集合中添加元素。返回值：无。
2. .update(item):像集合中批量添加元素(接收可迭代对象，例如：列表、元组、集合等)。返回值：无。

## 【删】
1. .remove(item):从集合中移除**指定元素**(若元素不存在，会报错)。返回值：无。
2. .discard(item):从集合中移除**指定元素**(若元素不存在，不报错)。返回值：无。
3. .pop():从集合中移除**任意**一个元素。返回值：移除的那个元素。
4. .clear():清空集合。返回值：无，
## 【改】 ---- 不支持改，需要 remove+add 的组合，来达到修改的效果。
## 【查】 ---- 不具备按位置访问的能力(没有下标，不支持切片)。【成员运算符：某个元素是否在集合中。】
元素 in 集合  ||  元素 not in 集合
```python
# 定义空集合
s1 = set()  
s2 = {}     # 这样定义出来的是：空字典
s3 = frozenset() # 定义空集合【实际意义不大】

# 增
s1.add(10)
print(s1)       # {10}
s1.update(20)
print(s1)       # {10, 20},顺序随机

# 成员运算符
s4 = {10, 20, 30, 40}
result1 = 10 in s4
result2 = 11 not in s4
print(result1)          # true
print(result2)          # true
```

## 集合·常用方法
1. 集合A.difference(集合B):找出集合A中，不同于集合B的元素(集合A　与　集合B　都不变)，返回值：一个新集合。
2. 集合A.difference_update(集合B):从集合A中，删除集合B中存在的元素(集合A会被修改，而集合B不会)，返回值：无。
3. 集合A.union(集合B):合并两个集合，集合A　和　集合B　都不变。返回值：一个新集合。
4. 集合A.issubset(集合B):判断集合A是否为集合B的子集。规则：如果集合A中的所有元素，都在集合B中，那就返回true，否则返回false。
5. 集合A.issuperset(集合B):判断集合A是否为集合B的超集。规则：如果集合A中，包含集合B的所有元素，那就返回true,否则返回false。
6. 集合A.isdisjoint(集合B):判断集合A和集合B是否没有交集。规则：如果没有交集，返回true,但凡有一个公共元素，就返回false。
```python
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {30, 40, 50}
result1 = s1.difference(s2)             # {10, 20}
result2 = s1.difference_update(s2)      # {10, 20}
result3 = s1.union(s2)                  # {70, 40, 30, 20, 10, 50, 60}
print(result1)      
print(result2, s2)                      # {10, 20},{30, 40, 50, 60, 70}
print(result3)

result4 = s2.issubset(s1)               # false
result5 = s2.issuperset(s3)             # true
result6 = s1.isdisjoint(s3)             # true
```
## 集合·数学运算
并集、交集、差集、对称差集:
```python
s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}
result1 = s1 | s2           # {10, 20, 30, 40, 50, 60, 70, 80, 90}
result2 = s1 & s2           # {40, 50, 60}
result3 = s2 - s1           # {70, 80, 90}
result4 = s1 ^ s2           # {10, 20, 30, 70, 80, 90}
```

## 集合·循环遍历
集合不能使用while循环直接遍历，但可以使用for循环进行遍历。【原因：while循环需要通过下标访问元素，而集合是无序的、没有下标】

# 6. 字典·dict
1. 对应关系：键key与值value的对应关系。
2. 字典中的键key不能重复，如果出现重复，则后写的会覆盖之前的。
3. 字典中的键key必须是不可变的类型，但值value可以是任意类型。 
4. 字典可以嵌套。
```python
d1 = {'张三': 87, '李四': 80, '王五': 99, '张三': 87}
print(d1)           # {'张三': 87, '李四': 80, '王五': 99}
d2 = {250: 72, '李四': 80, '王五': 99}
d3 = {('喝酒','抽烟'): 250, '李四': 80, '王五': 99}

# 字典嵌套
student_dict = {
   2026001:{'姓名':'jethro', '年龄': 24, '成绩': 100},
   2026002:{'姓名':'oldest', '年龄': 99, '成绩': 95},
   2026003:{'姓名':'Mai', '年龄': 30, '成绩': 90}
}
```

## 增删改查
1. 查询.get(value,'default words')
2. 增加 dict[key] = value
3. 修改：单个修改【增加也可以是修改，前提key已有】、批量修改【.update({key1: value1, key2: value2})】
4. 删除：
   1. del dict[key]
   2. .pop(key)：删除指定key所对应的那组键值对，并返回这个key所对应的值。
   3. .pop(key, 'default words')
```python
d1 = {'张三': 87, '李四': 80, '王五': 99}
result1 = d1.get('张三','sorry, this key is not exist!')
print(result1)          # 87

d1['赵六'] = 60
print(d1)               # {'张三': 87, '李四': 80, '王五': 99, '赵六': 60}

# 修改的写法和新增的写法一样。若字典中有对应的key，就是修改；若没有，就是新增
d1['张三'] = 88
print(d1)               # {'张三': 88, '李四': 80, '王五': 99, '赵六': 60}
# 批量修改
d1.update({'张三': 77, '李四': 88})
print(d1)               # {'张三': 77, '李四': 88, '王五': 99, '赵六': 60}

# 删除指定key所对应的那组键值对
del d1['赵六']
print(d1)               # {'张三': 77, '李四': 88, '王五': 99}
# 删除指定键值对,并反应这个key所对应的值
result2 = d1.pop('张三','delete error...')
print(result2)          # 77
print(d1)               # {'李四': 88, '王五': 99}
```
## 字典·常用方法
1. keys方法：用于获取字典中所有的键。返回值：dict_keys类型，和列表类似，可以被遍历，但要注意的是：不能通过下标访问元素。【借助内置的list函数，可以将其转化为list】
2. values方法：获取字典中所有的值。返回值：dict_values类型，和列表类似，可以被遍历，但要注意的是：不能通过下标访问元素。【借助内置的list函数，可以将其转化为list】
3. items方法：获取字典中所有的键值对。返回值：dict_items类型.(每组键值对以元组的形式呈现)
```python
d1 = {'张三': 87, '李四': 80, '王五': 99}
result1 = d1.keys()
print(result1)               # ('张三', '李四', '王五')
# 遍历
for item in result1:
    print(item)
# 将dict_keys转为list
l1 = list(result1)

result2 = d1.values()
print(result2)              # (87, 80, 99)
l2 = list(result2)

# item：获取所有键值对
result3 = d1.items()
print(result3)              # ([('张三': 87), ('李四': 80), ('王五': 99)])
```

## 字典·循环遍历【不可以用while，可以用for】
```python
d1 = {'张三': 87, '李四': 80, '王五': 99}
# 遍历整个字典
for key in d1:
    print(f'{key}的成绩是{d1[key]}')
# 遍历字典的所有key
for key in d1.keys():
    print(f'{key}的成绩是{d1[key]}')

```