import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['STHeiti']

# 1. 数据准备
np.random.seed(42)
N = 2000
X_np = np.random.rand(N, 1).astype(np.float32)
y_np = 3 * X_np + 2 + 0.3 * np.random.randn(N, 1).astype(np.float32)

X = torch.from_numpy(X_np)
y = torch.from_numpy(y_np)

# 2. 训练函数（可配置学习率和批量大小）
def train_model(lr, batch_size, epochs=50):
    """
    lr: 学习率
    batch_size: 批量大小（若为 None，表示全批量）
    epochs: 训练轮数
    返回: 损失历史, 最终w, 最终b, 总耗时
    """
    model = nn.Linear(1, 1)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=lr)

    # 构建 DataLoader
    if batch_size is None:
        # 全批量：把整个数据集作为一个 batch
        loader = [(X, y)]
    else:
        dataset = TensorDataset(X, y)
        loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    loss_history = []
    start_time = time.time()

    for epoch in range(epochs):
        epoch_loss = 0.0
        for batch_X, batch_y in loader:
            y_pred = model(batch_X)
            loss = criterion(y_pred, batch_y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item() * len(batch_X)

        # 记录每个 epoch 的平均损失
        loss_history.append(epoch_loss / N)

    elapsed = time.time() - start_time
    w = model.weight.item()
    b = model.bias.item()
    return loss_history, w, b, elapsed


# 3. 实验一：不同学习率的影响（固定批量大小=32）
print("=" * 70)
print("实验一：不同学习率的影响（批量大小=32，epochs=50）")
print("=" * 70)

learning_rates = [0.001, 0.01, 0.1, 0.5]
results_lr = {}

for lr in learning_rates:
    loss_hist, w, b, t = train_model(lr=lr, batch_size=32, epochs=50)
    results_lr[lr] = loss_hist
    print(f"学习率={lr:6.3f} | 最终Loss={loss_hist[-1]:.4f} | "
          f"w={w:.4f} | b={b:.4f} | 耗时={t:.3f}s")

# 可视化学习率对比
plt.figure(figsize=(10, 6))
for lr in learning_rates:
    plt.plot(results_lr[lr], label=f'lr={lr}')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('不同学习率的训练损失曲线（批量大小=32）')
plt.legend()
plt.grid(True, alpha=0.3)
plt.yscale('log')  # 对数坐标，便于观察差异
plt.tight_layout()
# plt.savefig('lr_comparison.png', dpi=150)
plt.show()


# 4. 实验二：不同批量大小的影响（固定学习率=0.05）
print("\n" + "=" * 70)
print("实验二：不同批量大小的影响（学习率=0.05，epochs=50）")
print("=" * 70)

batch_sizes = [8, 32, 128, None]  # None 表示全批量
results_bs = {}

for bs in batch_sizes:
    bs_name = "全批量" if bs is None else str(bs)
    loss_hist, w, b, t = train_model(lr=0.05, batch_size=bs, epochs=50)
    results_bs[bs_name] = loss_hist
    print(f"批量大小={bs_name:6s} | 最终Loss={loss_hist[-1]:.4f} | "
          f"w={w:.4f} | b={b:.4f} | 耗时={t:.3f}s")

# 可视化批量大小对比
plt.figure(figsize=(10, 6))
for bs_name, loss_hist in results_bs.items():
    plt.plot(loss_hist, label=f'batch={bs_name}')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('不同批量大小的训练损失曲线（学习率=0.05）')
plt.legend()
plt.grid(True, alpha=0.3)
plt.yscale('log')
plt.tight_layout()
# plt.savefig('bs_comparison.png', dpi=150)
plt.show()



# 5. 实验三：学习率过大导致发散的情况
print("\n" + "=" * 70)
print("实验三：学习率过大导致发散（学习率=2.0）")
print("=" * 70)

loss_hist, w, b, t = train_model(lr=2.0, batch_size=32, epochs=50)
print(f"学习率=2.0 | 最终Loss={loss_hist[-1]:.4f} | w={w:.4f} | b={b:.4f}")
print(f"前5个epoch的Loss: {[f'{l:.4f}' for l in loss_hist[:5]]}")
print(f"后5个epoch的Loss: {[f'{l:.4f}' for l in loss_hist[-5:]]}")