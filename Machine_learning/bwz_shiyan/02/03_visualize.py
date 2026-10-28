import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['STHeiti']

# ============================================================
# 1. 读取两个训练结果文件
# ============================================================
scratch = np.load('results/scratch_results.npz')
pytorch = np.load('results/pytorch_results.npz')

# 从各自的 npz 中取出数据
losses_s   = scratch['train_losses']
val_accs_s = scratch['val_accs']
preds_s    = scratch['test_preds']
y_test     = scratch['y_test']          # 两个文件的 y_test 应该一致
acc_s      = scratch['test_acc'].item()

losses_pt   = pytorch['train_losses']
val_accs_pt = pytorch['val_accs']
preds_pt    = pytorch['test_preds']
acc_pt      = pytorch['test_acc'].item()

print(f"从零实现准确率: {acc_s:.4f}")
print(f"PyTorch 准确率: {acc_pt:.4f}")

# ============================================================
# 2. 画图
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# 图1：训练损失对比
axes[0, 0].plot(losses_s, label='从零实现', linewidth=2)
axes[0, 0].plot(losses_pt, label='PyTorch', linewidth=2, linestyle='--')
axes[0, 0].set_xlabel('Epoch')
axes[0, 0].set_ylabel('Loss')
axes[0, 0].set_title('训练损失对比')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 图2：验证准确率对比
axes[0, 1].plot(val_accs_s, label='从零实现', linewidth=2)
axes[0, 1].plot(val_accs_pt, label='PyTorch', linewidth=2, linestyle='--')
axes[0, 1].set_xlabel('Epoch')
axes[0, 1].set_ylabel('Val Accuracy')
axes[0, 1].set_title('验证准确率对比')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# 图3：混淆矩阵（PyTorch）
cm = confusion_matrix(y_test, preds_pt)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1, 0])
axes[1, 0].set_xlabel('Predicted')
axes[1, 0].set_ylabel('True')
axes[1, 0].set_title(f'混淆矩阵（PyTorch, Acc={acc_pt:.4f}）')


plt.tight_layout()
plt.savefig('results/comparison.png', dpi=120)
plt.show()