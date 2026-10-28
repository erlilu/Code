import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

# 1.read dataset
dataset = pd.read_csv('../data/train.csv')


# 2. split dataset
X = dataset.drop('label', axis=1)
y = dataset['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# 3. feature engineering
scaler = MinMaxScaler()     # 归一化
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. define model and model training
model = LogisticRegression(max_iter=500)    # 默认softmax
model.fit(X_train, y_train)

# 5. model evaluation, calculating model accuracy
print(model.score(X_test, y_test))

# 6. test(预测某个新图像表示的数字)
digit = X_test[123, :].reshape(1, -1)
print(model.predict(digit))             # 预测值
print(y_test.iloc[123])                 # 真实值
print(model.predict_proba(digit))

# 7.show the picture
plt.imshow(digit.reshape(28, 28), cmap='gray')
plt.show()