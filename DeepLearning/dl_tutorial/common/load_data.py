import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def load_data():
    data = pd.read_csv('../data/train.csv')

    X = data.drop('label', axis=1)
    y = data['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

    preprocessor = MinMaxScaler()
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # 将数据都转换为ndarray
    y_train = y_train.values
    y_test = y_test.values

    return X_train, X_test, y_train, y_test


