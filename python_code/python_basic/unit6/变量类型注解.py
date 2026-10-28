# 变量类型注解：给变量加上类型说明，可增强代码的可读性、让 IDE 的提示更友好。
# 注意：可以先写变量的类型注解，以后再赋值
from typing import Union

num: int = 100
price: float  = 21.4
message: str = "Hello World!"
is_vip: bool = True


# hobby 是列表，并且列表中的所有元素必须是str
hobby: list[str] = ['抽烟', '喝酒', '烫头']

# color 是列表，并且列表中的元素，可以是str或者int类型
# Python 版本 3.10+ 允许采用这种方式
# color: list[str | int] = ['red', 1,]
# Python 版本 3.9 不允许将联合体类型编写为 X | Y


# 版本3.9 的标准写法【旧写法】
color: list[Union[str, int]] = ['red', 1,]
color.append('green')
color.append(33)

print(color)

