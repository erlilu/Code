import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model

"""
手动实现---梯度下降
1. 自己定义损失函数：MSE【向量的表示】
2. 自己定义计算梯度
"""

# 定义损失函数
def J(beta):
    return np.sum(np.square(X @ beta - y)) / n

# 定义计算梯度
def gradient(beta):
    return X.T @ (X @ beta - y) / n * 2

# 1.准备数据: 自变量X，因变量y
X = np.array([[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]])
y = np.array([[55], [65], [70], [75], [85], [50], [60], [72], [80], [58]])

# 2.数据处理
n = X.shape[0]      # 样本数
X  = np.hstack([np.ones((n, 1)), X])        # X添加一列1，与偏置beta0相乘

# 3.初始化参数、超参数
alpha = 0.01        # 步长【学习率】
epoch = 0           # 迭代次数
iter = 10000        # 得带次数

beta = np.array([[1], [1]])

# 定义列表，保存参数变化轨迹 【便于绘图】
beta0 = []
beta1 = []

# 4.重复迭代
# for i in range(iter):
#     grad = gradient(beta)       # 计算梯度
#     beta = beta -  alpha * grad        # 更新参数
# # 10轮打印一次
#     if i % 10 == 0:
#         print(f'beta: {beta.reshape(-1)}, iter: {i}, J: {J(beta)}')

# 计算到一定程度，没有必要浪费算力 【梯度不在变化时，直接结束迭代】
while (np.abs(grad := gradient(beta)) > 1e-10).any() and (iter := iter - 1) >= 0:       # 只要任意一个梯度向量满足，就继续执行
    beta0.append(beta[0, 0])
    beta1.append(beta[1, 0])

    beta = beta - alpha * grad
    
    if iter % 10 == 0:
        print(f"beta: {beta.reshape(-1)}, iter:{iter}, J: {J(beta)}")

print(iter)     # 节省的iter次数


plt.plot(beta0, beta1, color="blue")
plt.show()

