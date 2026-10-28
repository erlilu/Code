
# 闭包
def outer():
    num = 10

    def inner():
        nonlocal num
        num += 1
        print(num)
    return inner

f = outer()
f()
f()
f()

# 结论：
# 1. outer函数中，被inner所使用到的那些变量，会被封存到【闭包单元cell】中。
# 2.这些cell会组成一个__closure__元组，最终放在了inner函数身上。


# 打印__closure__元组
print(f.__closure__)

# 打印__closure__元组中的某一项
print(f.__closure__[0])

# 打印__closure__元组中的某一项的具体值
print(f.__closure__[0].cell_contents)

# 注意点
# 1.调用n次外层函数，就会得到n个不同的闭包，并且这些闭包之间互不影响。
# 2.内层函数中用到的外层变量是可变对象，多个闭包之间依然互不影响。

# 闭包的优点：
# 1. 可以记住状态：不用全局变量，也不用写类，就能在多次调用之间保存数据。
# 2. 可以做配置过的函数：先传一部分参数，把环境固定住，得到一个定制版函数。
# 3，可以实现简单的数据隐藏：外层变量对外不可见，只能通过内层函数访问。
# 4. 是装饰器(decorate)等高级用法的基础。

# 闭包的缺点
# 1.理解成本较高：对初学者不太友好，滥用会让代码难读。
# 2.如果闭包里引用了很大的对象，又长期不释放，可能会增加内存占用。
# 3.很多场景下，其实【类 + 实例属性】会更清晰，闭包不一定是最优解。

def beauty(char, n):
    def show_msg(msg):
        print(char * n + msg + char * n)
    return show_msg

show1 = beauty('*', 3)
show1('你好啊')
show1('北物资')

show2 = beauty('@', 3)
show2('你好啊')
show2('北物资')














