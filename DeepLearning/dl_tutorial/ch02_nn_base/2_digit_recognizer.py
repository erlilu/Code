import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from common.functions import sigmoid, softmax, identity


def get_data():
    data = pd.read_csv('../data/train.csv')

    X = data.drop('label', axis=1)
    y = data['label']

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

    # 归一化
    preprocessor = MinMaxScaler()
    x_train = preprocessor.fit_transform(x_train)
    x_test = preprocessor.transform(x_test)

    return x_test, y_test

# initialize nn
def init_network():
    network = joblib.load('../data/nn_sample')
    return network

# forward propagation
def forward(network, x):
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # 逐层进行计算传递
    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = identity(a3)
    return y

# mian
# 1. 获取测试数据
x, y = get_data()
print(x.shape, y.shape)

# 2. 创建模型（加载参数）
network = init_network()

# 3. 向前传播
y_proba = forward(network, x)    # y_proba.shape = (12600, 10)

# 4. 将分类概率转为分类标签，计算分类准确率
y_pred = np.argmax(y_proba, axis=1)
accuracy_cnt = np.sum(y_pred == y)
n = x.shape[0]
print('Accuracy: ', accuracy_cnt / n)

