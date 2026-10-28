import numpy as np

# 阶跃函数
def step_function0(x):
    if x > 0:
        return 1
    else:
        return 0


def step_function(x):
    return np.array(x > 0, dtype=int)


# sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def Tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

# def softmax(x):
#     return np.exp(x) / np.sum(np.exp(x))

# 优化后
def softmax(x):
    if x.ndim == 2:
        x = x.T             # 保证可以让每列参与计算
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T      # 转置回去
    else:
        x = x - np.max(x)       # 溢出对策
        return np.exp(x) / np.sum(np.exp(x))

'''
这里也可以不使用转置

def sigmoid(x):
    if x.ndim == 2:
        x = x - x.np.max(x, axis=1, keepdims=True))
        y = np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True))
        return y
    else:
        x = x - np.max(x) 
        return np.exp(x) / np.sum(np.exp(x))
'''

def identity(x):
    return x


if __name__ == '__main__':
    pass