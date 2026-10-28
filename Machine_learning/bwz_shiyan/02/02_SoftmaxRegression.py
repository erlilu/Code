import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['STHeiti']



DATA_PATH = '../data/train.csv'
df = pd.read_csv(DATA_PATH)
print(f"数据形状: {df.shape}")

# 分离标签和特征
y_all = df.iloc[:, 0].values.astype(np.int64)
X_all = df.iloc[:, 1:].values.astype(np.float32) / 255.0  # 归一化到 [0,1]

# 划分训练集 / 验证集 / 测试集（6:2:2）
X_train, X_temp, y_train, y_temp = train_test_split(
    X_all, y_all, test_size=0.4, random_state=42, stratify=y_all
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
)

print(f"训练集: {X_train.shape}, 验证集: {X_val.shape}, 测试集: {X_test.shape}")

# 限制 CPU 线程，避免 PyCharm 卡死
torch.set_num_threads(4)

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"使用设备: {device}")

# 数据留在 CPU，训练时才搬到 MPS
X_train_t = torch.from_numpy(X_train)
y_train_t = torch.from_numpy(y_train)
X_val_t   = torch.from_numpy(X_val)
y_val_t   = torch.from_numpy(y_val)
X_test_t  = torch.from_numpy(X_test)
y_test_t  = torch.from_numpy(y_test)

train_dataset = TensorDataset(X_train_t, y_train_t)
val_dataset   = TensorDataset(X_val_t, y_val_t)

# 模型
class SoftmaxNet(nn.Module):
    def __init__(self, n_features=784, n_classes=10):
        super().__init__()
        self.fc = nn.Linear(n_features, n_classes)

    def forward(self, x):
        return self.fc(x)


model = SoftmaxNet().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.9, weight_decay=1e-4)


def train_pytorch(model, optimizer, batch_size=256, epochs=20):
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader   = DataLoader(val_dataset, batch_size=512, shuffle=False)

    losses, val_accs = [], []
    best_acc, best_state = 0, None

    for epoch in range(epochs):
        model.train()
        epoch_loss, n_batches = 0, 0

        for bx, by in train_loader:
            # 只把当前 batch 搬到 MPS
            bx, by = bx.to(device), by.to(device)
            logits = model(bx)
            loss = criterion(logits, by)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1

        # 验证
        model.eval()
        correct, total = 0, 0
        with torch.no_grad():
            for bx, by in val_loader:
                bx, by = bx.to(device), by.to(device)
                preds = model(bx).argmax(dim=1)
                correct += (preds == by).sum().item()
                total += len(by)

        val_acc = correct / total
        losses.append(epoch_loss / n_batches)
        val_accs.append(val_acc)

        if val_acc > best_acc:
            best_acc = val_acc
            best_state = {k: v.clone() for k, v in model.state_dict().items()}

        if (epoch + 1) % 5 == 0:
            print(f"Epoch [{epoch+1}/{epochs}] Loss: {losses[-1]:.4f} | Val Acc: {val_acc:.4f}")

    model.load_state_dict(best_state)
    return losses, val_accs


print("\n" + "=" * 60)
print("PyTorch 实现 Softmax 回归")
print("=" * 60)

start = time.time()
losses_pt, val_accs_pt = train_pytorch(model, optimizer)
print(f"训练耗时: {time.time() - start:.1f}s")

# 测试集评估
model.eval()
with torch.no_grad():
    correct, total = 0, 0
    for i in range(0, len(X_test_t), 512):
        bx = X_test_t[i:i+512].to(device)
        by = y_test_t[i:i+512].to(device)
        preds = model(bx).argmax(dim=1)
        correct += (preds == by).sum().item()
        total += len(by)

test_acc_pt = correct / total
print(f"PyTorch 实现 - 测试准确率: {test_acc_pt:.4f}")



os.makedirs('results', exist_ok=True)

# 收集测试集全部预测（分批处理，避免一次性搬上 MPS）
all_preds = []
model.eval()
with torch.no_grad():
    for i in range(0, len(X_test_t), 512):
        bx = X_test_t[i:i+512].to(device)
        preds = model(bx).argmax(dim=1).cpu().numpy()
        all_preds.extend(preds)

np.savez('results/pytorch_results.npz',
         train_losses=np.array(losses_pt),
         val_accs=np.array(val_accs_pt),
         test_preds=np.array(all_preds),
         y_test=y_test,
         test_acc=test_acc_pt)

print("PyTorch 实现结果已保存到 results/pytorch_results.npz")