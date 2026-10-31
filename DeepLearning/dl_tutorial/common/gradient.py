import numpy as np
"""
中心差分
"""
# 数值微分
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

# 数值微分求梯度，传入x是一个向量
def _numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    # 遍历x中的特征
    for i in range(x.size):
        tmp = x[i]
        x[i] = tmp + h
        fxh1 = f(x)
        x[i] = tmp - h
        fxh2 = f(x)
        grad[i] = (fxh1 - fxh2) / (2*h)
        # 恢复x[i]的值
        x[i] = tmp
    return grad

# 传入X是一个矩阵
def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient(f, X)
    else:
        grad = np.zeros_like(X)
        for i, x in enumerate(X):
            grad[i] = numerical_gradient(f, x)
        return grad
