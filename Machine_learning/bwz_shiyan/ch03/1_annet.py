import os
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"

import gc
import time
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split

# 限制 CPU 线程，避免 PyCharm 卡死
torch.set_num_threads(4)

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"使用设备: {device}")

# ============================================================
# 1. 数据准备（只加载一次，全程留 CPU）
# ============================================================
df = pd.read_csv('../data/train.csv')
y_all = df.iloc[:, 0].values.astype(np.int64)
X_all = df.iloc[:, 1:].values.astype(np.float32) / 255.0
del df

# 控制内存：只取前 36000 条，再划分 24000/6000/6000
X_all, y_all = X_all[:36000], y_all[:36000]

X_train, X_temp, y_train, y_temp = train_test_split(
    X_all, y_all, test_size=1/3, random_state=42, stratify=y_all
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
)
del X_all, y_all, X_temp, y_temp

# 转 Tensor，留在 CPU
X_train_t = torch.from_numpy(X_train); y_train_t = torch.from_numpy(y_train)
X_val_t   = torch.from_numpy(X_val);   y_val_t   = torch.from_numpy(y_val)
X_test_t  = torch.from_numpy(X_test);  y_test_t  = torch.from_numpy(y_test)

print(f"训练集 {X_train_t.shape}, 验证集 {X_val_t.shape}, 测试集 {X_test_t.shape}")


# ============================================================
# 2. 可配置的全连接网络
# ============================================================
class FlexibleMLP(nn.Module):
    def __init__(self, input_dim=784, hidden_sizes=(256, 128),
                 num_classes=10, activation='relu',
                 dropout=0.0, use_bn=False):
        super().__init__()
        layers = []
        in_dim = input_dim
        for h in hidden_sizes:
            layers.append(nn.Linear(in_dim, h))
            if use_bn:
                layers.append(nn.BatchNorm1d(h))
            if activation == 'relu':
                layers.append(nn.ReLU())
            elif activation == 'sigmoid':
                layers.append(nn.Sigmoid())
            elif activation == 'tanh':
                layers.append(nn.Tanh())
            if dropout > 0:
                layers.append(nn.Dropout(dropout))
            in_dim = h
        layers.append(nn.Linear(in_dim, num_classes))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)  # 返回 logits


# ============================================================
# 3. 训练 + 评估函数
# ============================================================
def evaluate(model, loader, criterion, loss_type):
    model.eval()
    total_loss, correct, total = 0.0, 0, 0
    with torch.no_grad():
        for bx, by in loader:
            bx, by = bx.to(device), by.to(device)
            logits = model(bx)
            if loss_type == 'ce':
                loss = criterion(logits, by)
                preds = logits.argmax(dim=1)
            else:  # mse
                probs = torch.softmax(logits, dim=1)
                loss = criterion(probs, F.one_hot(by, 10).float())
                preds = logits.argmax(dim=1)
            total_loss += loss.item() * len(by)
            correct += (preds == by).sum().item()
            total += len(by)
    return total_loss / total, correct / total


def run_experiment(name, hidden_sizes=(256, 128), activation='relu',
                   dropout=0.0, use_bn=False, loss_type='ce',
                   lr=0.001, batch_size=128, weight_decay=0.0,
                   epochs=8, optimizer_name='Adam'):
    # 固定随机种子，保证对比公平
    torch.manual_seed(42)
    np.random.seed(42)

    model = FlexibleMLP(hidden_sizes=hidden_sizes, activation=activation,
                        dropout=dropout, use_bn=use_bn).to(device)

    if loss_type == 'ce':
        criterion = nn.CrossEntropyLoss()
    else:
        criterion = nn.MSELoss()

    if optimizer_name == 'Adam':
        optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    elif optimizer_name == 'SGD':
        optimizer = optim.SGD(model.parameters(), lr=lr, momentum=0.9,
                              weight_decay=weight_decay)
    else:
        optimizer = optim.RMSprop(model.parameters(), lr=lr, weight_decay=weight_decay)

    train_loader = DataLoader(TensorDataset(X_train_t, y_train_t),
                              batch_size=batch_size, shuffle=True,
                              num_workers=0, pin_memory=False)
    val_loader   = DataLoader(TensorDataset(X_val_t, y_val_t),
                              batch_size=512, shuffle=False,
                              num_workers=0, pin_memory=False)
    test_loader  = DataLoader(TensorDataset(X_test_t, y_test_t),
                              batch_size=512, shuffle=False,
                              num_workers=0, pin_memory=False)

    start = time.time()
    train_losses, val_losses, val_accs = [], [], []

    for epoch in range(epochs):
        model.train()
        epoch_loss, n_batches = 0.0, 0
        for bx, by in train_loader:
            bx, by = bx.to(device), by.to(device)
            logits = model(bx)
            if loss_type == 'ce':
                loss = criterion(logits, by)
            else:
                probs = torch.softmax(logits, dim=1)
                loss = criterion(probs, F.one_hot(by, 10).float())

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1

        train_losses.append(epoch_loss / n_batches)
        val_loss, val_acc = evaluate(model, val_loader, criterion, loss_type)
        val_losses.append(val_loss)
        val_accs.append(val_acc)

    elapsed = time.time() - start

    # 最终评估：训练误差、验证误差、测试损失、测试准确率
    train_loss, train_acc = evaluate(model, train_loader, criterion, loss_type)
    val_loss, val_acc = evaluate(model, val_loader, criterion, loss_type)
    test_loss, test_acc = evaluate(model, test_loader, criterion, loss_type)

    n_params = sum(p.numel() for p in model.parameters())

    result = {
        '实验': name,
        '参数量': n_params,
        '训练损失': round(train_loss, 4),
        '训练准确率': round(train_acc, 4),
        '验证损失': round(val_loss, 4),
        '验证准确率': round(val_acc, 4),
        '测试损失': round(test_loss, 4),
        '测试准确率': round(test_acc, 4),
        '耗时(s)': round(elapsed, 1),
    }
    print(f"{name:32s} | 测试Acc={test_acc:.4f} | 测试Loss={test_loss:.4f} | "
          f"参数={n_params} | {elapsed:.1f}s")

    # 内存清理
    del model, optimizer, train_loader, val_loader, test_loader
    gc.collect()
    if device.type == 'mps':
        torch.mps.empty_cache()

    return result


# ============================================================
# 4. 实验 1：网络层数与宽度
# ============================================================
print("\n" + "="*80)
print("实验1：网络结构对比（ReLU, CE, Adam, lr=0.001, batch=128）")
print("="*80)

results = []
results.append(run_experiment("1层-128", hidden_sizes=(128,)))
results.append(run_experiment("2层-256-128", hidden_sizes=(256, 128)))
results.append(run_experiment("3层-256-128-64", hidden_sizes=(256, 128, 64)))
results.append(run_experiment("2层宽-512-256", hidden_sizes=(512, 256)))


# ============================================================
# 5. 实验 2：激活函数
# ============================================================
print("\n" + "="*80)
print("实验2：激活函数对比（2层-256-128, CE, Adam）")
print("="*80)

results.append(run_experiment("ReLU", hidden_sizes=(256, 128), activation='relu'))
results.append(run_experiment("Sigmoid", hidden_sizes=(256, 128), activation='sigmoid'))


# ============================================================
# 6. 实验 3：损失函数
# ============================================================
print("\n" + "="*80)
print("实验3：损失函数对比（2层-256-128, ReLU）")
print("="*80)

results.append(run_experiment("交叉熵损失", hidden_sizes=(256, 128), loss_type='ce'))
results.append(run_experiment("均方误差损失", hidden_sizes=(256, 128), loss_type='mse'))


# ============================================================
# 7. 实验 4：学习率与批量大小
# ============================================================
print("\n" + "="*80)
print("实验4：学习率与批量大小（2层-256-128, ReLU, CE）")
print("="*80)

for lr in [0.0001, 0.001, 0.01]:
    results.append(run_experiment(f"lr={lr}", hidden_sizes=(256, 128), lr=lr))

for bs in [64, 128, 256]:
    results.append(run_experiment(f"batch={bs}", hidden_sizes=(256, 128), batch_size=bs))


# ============================================================
# 8. 实验 5：L2 正则化
# ============================================================
print("\n" + "="*80)
print("实验5：L2 正则化（2层-256-128, ReLU, CE, Adam）")
print("="*80)

for wd in [0.0, 1e-4, 1e-2]:
    results.append(run_experiment(f"weight_decay={wd}", hidden_sizes=(256, 128),
                                  weight_decay=wd))


# ============================================================
# 9. 实验 6：Dropout 与 BatchNorm
# ============================================================
print("\n" + "="*80)
print("实验6：Dropout / BatchNorm（2层-256-128, ReLU, CE）")
print("="*80)

results.append(run_experiment("无Dropout无BN", hidden_sizes=(256, 128)))
results.append(run_experiment("Dropout=0.3", hidden_sizes=(256, 128), dropout=0.3))
results.append(run_experiment("BatchNorm", hidden_sizes=(256, 128), use_bn=True))
results.append(run_experiment("Dropout+BN", hidden_sizes=(256, 128), dropout=0.3, use_bn=True))


# ============================================================
# 10. 汇总结果
# ============================================================
print("\n" + "="*80)
print("全部实验结果汇总")
print("="*80)
result_df = pd.DataFrame(results)
print(result_df.to_string(index=False))
result_df.to_csv('experiment_results.csv', index=False, encoding='utf-8-sig')
print("\n结果已保存到 experiment_results.csv")