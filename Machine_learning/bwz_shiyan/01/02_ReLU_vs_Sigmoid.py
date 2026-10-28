import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# 1. 数据集准备（二分类，月牙形）
X_np, y_np = make_moons(n_samples=1000, noise=0.2, random_state=42)

# 标准化
scaler = StandardScaler()
X_np = scaler.fit_transform(X_np)

# 划分训练集/测试集
X_train, X_test, y_train, y_test = train_test_split(
    X_np, y_np, test_size=0.3, random_state=42
)

# 转为张量
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).reshape(-1, 1)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32).reshape(-1, 1)

# 2. 定义一个可替换激活函数的简单网络
class SimpleNet(nn.Module):
    def __init__(self, activation):
        super().__init__()
        self.fc1 = nn.Linear(2, 16)      # 输入2维，隐藏层16个神经元
        self.fc2 = nn.Linear(16, 1)      # 输出1维（二分类）
        self.activation = activation     # 激活函数实例

    def forward(self, x):
        x = self.activation(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))   # 输出层用 Sigmoid 得到概率
        return x

# 3. 训练与评估函数
def train_and_evaluate(activation_name, activation_fn, epochs=200):
    model = SimpleNet(activation_fn)
    criterion = nn.BCELoss()  # 二分类交叉熵
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(epochs):
        model.train()
        y_pred = model(X_train)
        loss = criterion(y_pred, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # 评估
    model.eval()
    with torch.no_grad():
        y_pred_test = model(X_test)
        y_pred_label = (y_pred_test > 0.5).float()
        acc = (y_pred_label == y_test).float().mean().item()
    print(f"激活函数: {activation_name:8s} | 测试准确率: {acc:.4f}")
    return acc


# 4. 对比 ReLU 与 Sigmoid
print("=" * 50)
print("比较不同激活函数对分类性能的影响")
print("=" * 50)

acc_relu = train_and_evaluate("ReLU", nn.ReLU())
acc_sigmoid = train_and_evaluate("Sigmoid", nn.Sigmoid())

# 简单结论
print("\n结论:")
if acc_relu > acc_sigmoid:
    print(f"ReLU 比 Sigmoid 高 {acc_relu - acc_sigmoid:.4f}")
else:
    print(f"Sigmoid 比 ReLU 高 {acc_sigmoid - acc_relu:.4f}")

