import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs     # 按照簇中心生成
from matplotlib import rcParams
rcParams['font.sans-serif'] = 'STHeiti'

# 1. 生成数据
X,y = make_blobs(n_samples=500,centers=3,cluster_std=2,random_state=0)

# 画图
fig, ax = plt.subplots(2,figsize=(8,8))

ax[0].scatter(X[:, 0], X[:, 1], c='gray', s=50, alpha=0.8, label='raw data')
ax[0].set_title('raw data')
ax[0].legend()

# 2. 定义模型并聚类
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# 3. 获取聚类结果
centers = kmeans.cluster_centers_

# 4. 预测，得到所有样本点的分类标签
y_pred = kmeans.predict(X)

# 画出聚类结果
ax[1].scatter(X[:, 0], X[:, 1], c=y_pred, s=50, alpha=0.8, label='predicted data')
ax[1].scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.8, label='cluster centers')
ax[1].set_title('predicted and cluster centers')
ax[1].legend()
plt.show()
