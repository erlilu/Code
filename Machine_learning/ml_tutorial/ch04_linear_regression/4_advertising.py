import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler    # 标准化
from sklearn.linear_model import LinearRegression, SGDRegressor     # 线性回归模型：正规方程法和SGD
from sklearn.metrics import mean_squared_error      # 均方误差损失函数


# 1. load dataset
dataset = pd.read_csv('../data/advertising.csv')

dataset.dropna(inplace=True)
dataset.drop(columns=dataset.columns[0], axis=1, inplace=True)

print(dataset.info())
print(dataset.head())

# 2. split dataset
X = dataset.drop(columns='Sales', axis=1)
y = dataset['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# 3. feature engineering: Standar
scaler = StandardScaler()
X_trian = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. create model & model training
# 4.1 正规方程法
model_lr = LinearRegression()
model_lr.fit(X_trian, y_train)

print("lr coefficient: ", model_lr.coef_)
print("lr intercept: ", model_lr.intercept_)

# 4.2 SGD
model_sgd = SGDRegressor()
model_sgd.fit(X_trian, y_train)

print("sgd coefficient: ", model_sgd.coef_)
print("sgd intercept: ", model_sgd.intercept_)

# 5. prediction
y_pred1 = model_lr.predict(X_test)
y_pred2 = model_sgd.predict(X_test)

# 6. use MSE to evaluation
print('lr MSE:', mean_squared_error(y_test, y_pred1))
print('sgd MSE:', mean_squared_error(y_test, y_pred2))