import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso, Ridge   # 线性回归模型,Lasso回归，岭回归
from sklearn.preprocessing import PolynomialFeatures    # 构建多项式特征
from sklearn.model_selection import train_test_split    # 划分训练集和测试集
from sklearn.metrics import mean_squared_error          # 均方误差损失函数MSE

plt.rcParams['font.sans-serif'] = ['STHeiti']



"""
测试正则化：不正则化、Lasso正则化、Ridge正则化
1. 生成数据
2. 划分训练集和测试计集（验证集）
"""
# 1. 生成数据
X = np.linspace(-3, 3, 300).reshape(-1, 1)      # (-1, 1),表示变为1列，行数自动计算【-1】
y = np.sin(X) + np.random.uniform(-0.5, 0.5, 300).reshape(-1, 1)
# 画出散点图(2✖️3个子图)
fig, ax = plt.subplots(2, 3, figsize=(15, 8))
ax[0, 0].scatter(X, y, c='y')
ax[0, 1].scatter(X, y, c='y')
ax[0, 2].scatter(X, y, c='y')

# 2. 划分训练集和测试计集（验证集）
trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.2, random_state=42)


poly20 = PolynomialFeatures(degree=20)    # 五次项，单会加一个0次项
x_train = poly20.fit_transform(trainX)
x_test = poly20.fit_transform(testX)
print(x_train.shape, x_test.shape)    # (240, 21) (60, 21)


"""
3. 定义模型（线性回归模型）
4. 训练模型
5. 预测结果，计算损失loss function
"""

'''不正则化'''
# 3. 定义模型（线性回归模型）不正则化
model = LinearRegression()

# 4. 训练模型
model.fit(x_train, trainY)

# 5. 预测结果，计算损失loss function
y_pred1 = model.predict(x_test)        # 测试数据的预测值
test_loss = mean_squared_error(testY, y_pred1)       # 测试误差
train_loss1 = mean_squared_error(trainY, model.predict(x_train)) # 训练误差

# 画出拟合曲线，并写出训练误差和测试误差
ax[0, 0].plot(X, model.predict(poly20.fit_transform(X)), 'r' )
ax[0, 0].text(-3, 1 ,f'test loss is :{test_loss:.4f}')
ax[0, 0].text(-3, 1.3, f"train loss is :{train_loss1:.4f}")
# 画出所有系数的直方图
ax[1, 0].bar(np.arange(21), model.coef_.reshape(-1))



'''Lasso正则化'''
# 3. 定义模型（线性回归模型）
lasso = Lasso(alpha=0.01)        # alpha是超参数

# 4. 训练模型
lasso.fit(x_train, trainY)

# 5. 预测结果，计算损失loss function
y_pred1 = lasso.predict(x_test)        # 测试数据的预测值
test_loss = mean_squared_error(testY, y_pred1)       # 测试误差
train_loss1 = mean_squared_error(trainY, lasso.predict(x_train)) # 训练误差

# 画出拟合曲线，并写出训练误差和测试误差
ax[0, 1].plot(X, lasso.predict(poly20.fit_transform(X)), 'r' )
ax[0, 1].text(-3, 1 ,f'test loss is :{test_loss:.4f}')
ax[0, 1].text(-3, 1.3, f"train loss is :{train_loss1:.4f}")
# 画出所有系数的直方图
ax[1, 1].bar(np.arange(21), lasso.coef_.reshape(-1))


'''Ridge正则化'''
# 3. 定义模型（线性回归模型）
ridge = Ridge(alpha=1)        # alpha是超参数

# 4. 训练模型
ridge.fit(x_train, trainY)

# 5. 预测结果，计算损失loss function
y_pred1 = ridge.predict(x_test)        # 测试数据的预测值
test_loss = mean_squared_error(testY, y_pred1)       # 测试误差
train_loss1 = mean_squared_error(trainY, ridge.predict(x_train)) # 训练误差

# 画出拟合曲线，并写出训练误差和测试误差
ax[0, 2].plot(X, ridge.predict(poly20.fit_transform(X)), 'r' )
ax[0, 2].text(-3, 1 ,f'test loss is :{test_loss:.4f}')
ax[0, 2].text(-3, 1.3, f"train loss is :{train_loss1:.4f}")
# 画出所有系数的直方图
ax[1, 2].bar(np.arange(21), ridge.coef_.reshape(-1))

plt.show()