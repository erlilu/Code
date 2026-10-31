import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from common.load_data import load_data
from two_layer_net import TwoLayerNet

x_train, x_test, t_train, t_test = load_data()

network = TwoLayerNet(784, 50, 10)

# 设置相关参数
train_size = x_train.shape[0]       # 训练集的数量
num_epochs = 10                     # 整个训练集训练次数，epoch
batch_size = 100                    # 每次训练的样本量
learning_rate = 0.1                 # 学习率
iter_per_epoch = np.ceil(train_size / batch_size)   # 每个epoch中的迭代次数
iters_num = int(num_epochs * iter_per_epoch)    # 总循环次数


train_loss_list = []
train_acc_list = []
test_acc_list = []


# 循环迭代，用梯度下降法训练模型
for i in range(iters_num):
    # 随机选择批量数据
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 计算梯度
    grad = network.numerical_gradient(x_batch, t_batch)
    print('gradient======', i)
    # 更新参数
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    # 计算并保存当前的训练损失
    loss = network.loss(x_train, t_train)
    train_loss_list.append(loss)

    # 完成每次epoch迭代，就计算保存训练和测试准确率
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print('Epoch:{}, loss:{}, train_acc:{}, test_acc:{}'.format(i, loss, train_acc, test_acc))


x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train_acc', color='blue')
plt.plot(x, test_acc_list, label='test_acc', linestyle='--', color='red')
plt.legend(loc='lower right')
plt.show()
