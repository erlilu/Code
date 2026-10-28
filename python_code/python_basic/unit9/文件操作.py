
# 操作文件标准流程
# region
# file = open(file='西瓜数据集 3.0α.txt', mode='rt', encoding='utf-8')
#
# # result = file.read()
# # print(result)
#
# while True:
#     result = file.read(100)
#     if result == '':
#         break
#     print(result)
# file.close()
# endregion

# readline
# region
# file = open('test.txt', 'rt')
# r1 = file.readline()
# r2 = file.readline()
# r3 = file.readline()
# r4 = file.readline()
# print(r1,end='')
# print(r2,end='')
# print(r3,end='')
# print(r4,end='')
# print(r1)
# endregion

# readlines
# region
# file = open('test.txt', 'rt')
#
# result = file.readlines()
# print(result)
# file.close()
# endregion

# 最佳实践，使用with
with open('西瓜数据集 3.0α.txt', 'rt') as file:
    # result = file.read()
    # print(result)
    for line in file:
        print(line.rstrip())