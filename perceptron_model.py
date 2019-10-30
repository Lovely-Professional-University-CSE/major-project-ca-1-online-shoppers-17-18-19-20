import numpy as np
import pandas as pd
data=pd.read_csv('online_shoppers_intention.csv')
print(data.head())
data.shape
data.describe
data.columns
data.dtypes
data1=pd.get_dummies(data)
print(data1.head())
data1.columns
data1.shape
data.shape
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data['Revenue'] = le.fit_transform(data['Revenue'])
data['Revenue'].value_counts()
y=data['Revenue']


X=data1.drop(['Revenue'],axis=1)
print(X.shape)
print(y.shape)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

print("Shape of x_train :", x_train.shape)
print("Shape of y_train :", y_train.shape)
print("Shape of x_test :", x_test.shape)
print("Shape of y_test :", y_test.shape)
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
"""from sklearn.decomposition import PCA

pca = PCA(n_components = None)

x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)"""
print(x_train.shape)
print(x_test.shape)
print(y_test.shape)
print(y_train.shape)
class Perceptron(object):

        def __init__(self, eta, n_iter):
                self.eta = eta
                self.n_iter = n_iter

        def fit(self, X, y):

                self.w_ = np.zeros(1 + X.shape[1])
                self.errors_=[]
                for _ in range(self.n_iter):
                        errors=0
                        for xi, target in zip(X, y):
                                error = target - self.predict(xi)
                                if error != 0:
                                        update = self.eta * error
                                        self.w_[1:] += update * xi
                                        self.w_[0] += update
                                        errors+=int(update!=0.0)
                        self.errors_.append(errors)
                return self

        def net_input(self, X):
                return np.dot(X, self.w_[1:]) + self.w_[0]

        def predict(self, X):
                return np.where(self.net_input(X) >= 0.0, 0, 1)

import matplotlib.pyplot as plt
model = Perceptron(n_iter=1000,eta=0.28)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print('misclassified samples: %d'%(y_test!=y_pred).sum())#compute
from sklearn.metrics import accuracy_score
print('Accuracy:%.2f'%accuracy_score(y_test,y_pred))
plt.show()
