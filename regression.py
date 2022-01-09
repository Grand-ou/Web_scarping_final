## 導入所需的套件
## 導入Python數據處理套件
from re import T
import numpy as np
import pandas as pd
## 導入視覺化套件
import matplotlib.pyplot as plt
## 導入Sklearn套件
## 導入將數據集拆成訓練集與測試集的套件
from sklearn.model_selection import train_test_split
## 導入迴歸模型套件
from sklearn.linear_model import LinearRegression

## 導入數據集

dataset = pd.read_csv("process_data.csv")
dataset.drop(['隊伍', '日期'], inplace=True, axis=1)
y = dataset['勝負'].values
dataset.drop('勝負', inplace=True, axis=1)
X = dataset.values
print(X.shape)

## 將數據集拆成訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

## 訓練與建構迴歸模型
regressor = LinearRegression()
regressor.fit(X_train, y_train)

## 計算出截距值與係數值
w_0 = regressor.intercept_
w_1 = regressor.coef_

print('Interception : ', w_0)
print('Coeficient : ', w_1)
## 迴歸模型的準確度
score = regressor.score(X_test, y_test)
print('Score: ', score)
print('Accuracy: ' + str(score*100) + '%')
## 拿訓練好的迴歸模型預測測試集資料的目標值(依變數)
y_pred = regressor.predict(X_test)
print('Predict : ', y_pred)

## 視覺化迴歸模型與訓練集的關聯
# plt.scatter(X_train, y_train, color = 'red')
# plt.plot(X_train, regressor.predict(X_train), color = 'blue')
# plt.title('Salary vs Learning Hours (trainning set)')
# plt.xlabel("Hours of Learning per Month")
# plt.ylabel("Salary")
# plt.show()
# ## 視覺化迴歸模型與測試集的關聯
# plt.scatter(X_test, y_test, color = 'red')
# plt.plot(X_test, regressor.predict(X_test), color = 'blue')
# plt.title('Salary vs Learning Hours (test set)')
# plt.xlabel("Hours of Learning per Month")
# plt.ylabel("Salary")
# plt.show()