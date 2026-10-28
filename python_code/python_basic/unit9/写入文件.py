import time
# 1. file：要操作的文件路径
# 2. mode：文件的打开模式
#    - r：读取（默认值）
#    - w：写入，并先截断文件【截断文件 == 清空文件】
#    - x：排它性创建，如果文件已存在，则创建失败。
#    - a：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#    - b：二进制模式
#    - t：文本模式（默认值）
#    - +：打开用于更新（读取与写入）
# 3. encoding：字符编码

# 测试 w 模式
# with open('test.txt', 'wt', encoding='utf-8') as f:
#     f.write('hello world')


# 测试 x 模式
# with open('test_x.txt', 'xt', encoding='utf-8') as f:
#     f.write('hello world!')

# 测试 a 模式
# with open('test.txt', 'at', encoding='utf-8') as f:
#     f.write('hello world!')


# 测试 flush 方法
# 让写入的文件不用一直存放在缓冲区，执行flush，直接从缓冲区写入文件
with open('test.txt','at', encoding='utf-8') as f:
    f.write('hi\n')
    f.write('I will use flush function\n')
    f.flush()
    time.sleep(1000)
    f.write('this is detail after flush function\n')
    f.write('hi\n')


# 测试 rt+， seek方法
# with open('test.txt', 'rt+', encoding='utf-8') as f:
#     f.seek(0, 2)
#     f.write('你好')

# 测试 wt+
# with open('test.txt', 'wt+', encoding='utf-8') as f:
#     f.write('hello world')
#     result = f.read()         # 由于指针问题，result找不到内容


# 测试 xt+
# with open('test.txt', 'xt+', encoding='utf-8') as f:
#     f.seek(0)
#     result = f.read()
#     print(result)
