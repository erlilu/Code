import pandas as pd
from IPython.terminal import pt_inputhooks
from sklearn.model_selection import train_test_split, GridSearchCV      # model evaluation
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import joblib

# 1. load data set
heart_disease_data = pd.read_csv("../data/heart_disease.csv")

# handle missing values
heart_disease_data.dropna(inplace=True)

heart_disease_data.info()
print(heart_disease_data.head())


# 2. dataset splitting
# split features and labels
X = heart_disease_data.drop('是否患有心脏病', axis=1)
y = heart_disease_data['是否患有心脏病']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# 3.feature engineering
# numerical features
numerical_features = ['年龄', '静息血压' , '胆固醇', '最大心率', '运动后的ST下降', '主血管数量']
# categorical features
categorical_features = ['胸痛类型', '静息心电图结果', '峰值ST段的斜率', '地中海贫血']
# binary feature
binary_features = ['性别', '空腹血糖', '运动性心绞痛']

# create a column transformer
column_transformer = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features), # add words- "drop=first"
        ('binary', 'passthrough', binary_features)      # no action to pass
    ]
)
# features transform
X_train = column_transformer.fit_transform(X_train)
X_test = column_transformer.transform(X_test)       # 直接是用训练后的参数转换，不要fit

print(X_train.shape, X_test.shape)

# # 4.create model
# knn = KNeighborsClassifier(n_neighbors=3)
# # 5.model training
# knn.fit(X_train, y_train)
#
# # 6.model evaluation, calculating model accuracy
# score = knn.score(X_test, y_test)
# print(score)

# # 7. save model
# joblib.dump(value=knn, filename='knn_model.pkl')

# # loading model to predict for new data
# knn_loaded = joblib.load('knn_model.pkl')
# y_pred = knn_loaded.predict(X_test[10:11])
# print(f'prediction result: {y_pred}, actual result: {y_test[10]}')


'''
模型评估、超参数调优
model evaluation, hyperparameter tuning
'''
# 创建KNN分类器
knn = KNeighborsClassifier()

# 定义网格搜素参数列表
param_grid = {
    'n_neighbors': list(range(1, 11)),
    'weights': ['uniform', 'distance']
}                   # 传入K的取值、权重

grid_search_cv = GridSearchCV(estimator=knn,param_grid=param_grid, cv=10)   # 10折验证

# 模型训练
grid_search_cv.fit(X_train, y_train)

# 打印模型评估结果
results = pd.DataFrame(grid_search_cv.cv_results_).to_string()
print(results)

# 直接获取最佳模型和最佳得分
print(grid_search_cv.best_estimator_)
print(grid_search_cv.best_params_)
print(grid_search_cv.best_score_)

# 使用最佳模型，进行测试评估
knn = grid_search_cv.best_estimator_
print(knn.score(X_test, y_test))

