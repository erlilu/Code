import numpy as np
from common.functions import sigmoid, identity

"""
简单神经网络的实现：
- 三层网络的实现
- 输入层【1】
    - 第0层：2个输入参数x1, x2
- 隐藏层【2】：
    - 第1层：3个神经元（2，3）+（3,）
    - 第2层：2个神经元 (3,2) + (2,)
- 输出层【1】
    - 第3层：2个输出 (2,2) + (2,)
"""
# 初始化网络
def init_network():
    network = {}
    # the first floor
    network['W1'] = np.array([
        [0.1, 0.3, 0.5],
        [0.2, 0.4, 0.6],
    ])
    network['b1'] = np.array([0.1, 0.2, 0.3])

    # the second floor
    network['W2'] = np.array([
        [0.1, 0.4],
        [0.2, 0.5],
        [0.3, 0.6],
    ])
    network['b2'] = np.array([0.1, 0.2])

    # the third floor
    network['W3'] = np.array([
        [0.1, 0.3],
        [0.2, 0.4],
    ])
    network['b3'] = np.array([0.1, 0.2])

    return network

# 前向传播
def forward(network, x):
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # 逐层进行计算传递
    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, w3) + b3
    y = identity(a3)

    return y

# 测试主流程
network = init_network()
y = forward(network, np.array([1.0, 0.5]))
print(y)

