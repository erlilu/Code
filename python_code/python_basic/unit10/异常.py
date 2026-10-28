"""
异常不同于错误，解释器可以执行，能够通过异常处理机制解决
"""
from cgitb import reset

try:
    a = int(input('please input the first number: '))
    b = int(input('please input the second number: '))
    result1 = a / b
    print(f'the result is {result1}')
except (ZeroDivisionError, ValueError, Exception) as e:
    if isinstance(e, ZeroDivisionError):
        print('程序异常：0不能作为除数')
    elif isinstance(e, ValueError):
        print('程序异常：您输入的必须是数字')
    else:
        print(f'程序异常{e}')
else:
    print('一切顺利，try中的代码没有什么异常！')
finally:
    print('无论有没有异常，程序结束！')



# 自定义异常类
class SchoolNameError(Exception):
    def __init__(self, msg):
        super().__init__('【校名异常】' + msg)


def check_school_name(name):
    if len(name) > 10:
        raise SchoolNameError('学校名过长')
    else:
        print('学校名是合法的')

check_school_name(input('please input the school name: '))
