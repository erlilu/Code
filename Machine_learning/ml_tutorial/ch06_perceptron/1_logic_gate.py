import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    # 直接使用矩阵计算的结果
    res = w @ x + b
    if res > 0:
        return 1
    else:
        return 0

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    res = w @ x + b
    if res > 0:
        return 1
    else:
        return 0

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    res = w @ x + b
    if res > 0:
        return 1
    else:
        return 0

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

# test
print('-----------AND----------------')
print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))
print('-----------NAND----------------')
print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))
print('-----------OR----------------')
print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))

