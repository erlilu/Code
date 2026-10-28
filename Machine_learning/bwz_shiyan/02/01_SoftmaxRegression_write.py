import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns

# ============================================================
# 读取 train.csv
# ============================================================
DATA_PATH = '../data/train.csv'  # 改成你的实际路径

df = pd.read_csv(DATA_PATH)
print(f"数据形状: {df.shape}")  # 期望 (42000, 785)

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


# 1. 模型设计
class SoftmaxRegression:
    def __init__(self, n_features=784, n_classes=10):
        # 小随机数初始化，避免对称性
        self.W = np.random.randn(n_features, n_classes) * 0.01
        self.b = np.zeros(n_classes)

    def softmax(self, z):
        # 减最大值防止指数溢出
        z = z - np.max(z, axis=1, keepdims=True)
        exp_z = np.exp(z)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def forward(self, X):
        return self.softmax(X @ self.W + self.b)

    def cross_entropy_loss(self, y_pred, y_true, reg=1e-4):
        # 交叉熵 + L2 正则
        n = len(y_true)
        log_likelihood = -np.log(y_pred[np.arange(n), y_true] + 1e-10)
        loss = np.mean(log_likelihood) + 0.5 * reg * np.sum(self.W ** 2)
        return loss

    def backward(self, X, y_pred, y_true, reg=1e-4):
        n = len(y_true)
        # one-hot 编码
        y_onehot = np.zeros_like(y_pred)
        y_onehot[np.arange(n), y_true] = 1
        # 梯度
        dz = (y_pred - y_onehot) / n
        dW = X.T @ dz + reg * self.W
        db = np.sum(dz, axis=0)
        return dW, db

    def predict(self, X):
        return np.argmax(self.forward(X), axis=1)


# 2. 损失函数与优化器（手写 SGD）
def train_scratch(model, X_train, y_train, X_val, y_val,
                  lr=0.1, batch_size=64, epochs=20, reg=1e-4):
    n = len(y_train)
    train_losses, val_accs = [], []
    best_val_acc = 0
    best_params = None

    for epoch in range(epochs):
        idx = np.random.permutation(n)
        X_shuf, y_shuf = X_train[idx], y_train[idx]
        epoch_loss = 0
        n_batches = 0

        for i in range(0, n, batch_size):
            X_batch = X_shuf[i:i+batch_size]
            y_batch = y_shuf[i:i+batch_size]

            y_pred = model.forward(X_batch)
            loss = model.cross_entropy_loss(y_pred, y_batch, reg)
            dW, db = model.backward(X_batch, y_pred, y_batch, reg)

            # SGD 更新
            model.W -= lr * dW
            model.b -= lr * db

            epoch_loss += loss
            n_batches += 1

        # 验证
        val_acc = np.mean(model.predict(X_val) == y_val)
        train_losses.append(epoch_loss / n_batches)
        val_accs.append(val_acc)

        # 保存最优参数
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_params = (model.W.copy(), model.b.copy())

        if (epoch + 1) % 5 == 0:
            print(f"Epoch [{epoch+1}/{epochs}] Loss: {train_losses[-1]:.4f} | "
                  f"Val Acc: {val_acc:.4f}")

    # 恢复最优参数
    model.W, model.b = best_params
    return train_losses, val_accs


# 3. 训练与评估
print("\n" + "="*60)
print("从零实现 Softmax 回归")
print("="*60)

model_scratch = SoftmaxRegression()
start = time.time()
losses_s, val_accs_s = train_scratch(
    model_scratch, X_train, y_train, X_val, y_val,
    lr=0.1, batch_size=64, epochs=20
)
scratch_time = time.time() - start

# 测试集评估
y_pred_s = model_scratch.predict(X_test)
test_acc_s = np.mean(y_pred_s == y_test)
print(f"\n从零实现 - 测试集准确率: {test_acc_s:.4f}, 训练耗时: {scratch_time:.1f}s")


# 创建结果目录
os.makedirs('results', exist_ok=True)

# 保存训练过程 + 测试结果
np.savez('results/scratch_results.npz',
         train_losses=np.array(losses_s),          # 训练损失曲线
         val_accs=np.array(val_accs_s),            # 验证准确率曲线
         test_preds=model_scratch.predict(X_test), # 测试集预测标签
         y_test=y_test,                            # 测试集真实标签
         test_acc=test_acc_s)                      # 测试集准确率

print("从零实现结果已保存到 results/scratch_results.npz")