import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] ='STHeiti'

# 1. 数据集准备
# 生成 y = 3x + 2 + 噪声
np.random.seed(42)
X_np = np.random.rand(100, 1).astype(np.float32)  # 100个样本，1个特征
y_np = 3 * X_np + 2 + 0.1 * np.random.randn(100, 1).astype(np.float32)

# 转为 PyTorch 张量
X = torch.from_numpy(X_np)
y = torch.from_numpy(y_np)

# 2. 模型设计
# 线性回归：输入1维，输出1维，相当于 y = wx + b
model = nn.Linear(in_features=1, out_features=1)

# 3. 损失函数与优化器
criterion = nn.MSELoss()                     # 均方误差
optimizer = optim.SGD(model.parameters(), lr=0.1)  # 随机梯度下降


# 4. 模型训练
epochs = 200
for epoch in range(epochs):
    # 前向传播
    y_pred = model(X)
    loss = criterion(y_pred, y)

    # 反向传播与优化
    optimizer.zero_grad()   # 清空梯度
    loss.backward()         # 计算梯度
    optimizer.step()        # 更新参数

    if (epoch + 1) % 50 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# 查看训练后的参数
w, b = model.weight.item(), model.bias.item()
print(f"\n训练结果: w = {w:.4f}, b = {b:.4f}  (真实值 w=3, b=2)")

# 可视化
plt.scatter(X_np, y_np, label='真实数据', alpha=0.6)
plt.plot(X_np, model(X).detach().numpy(), color='red', linewidth=2, label='拟合直线')
plt.legend()
plt.title('PyTorch 线性回归')
# plt.savefig('pytorch_basic.png', dpi=150)
plt.show()
