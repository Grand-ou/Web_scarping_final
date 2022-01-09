from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
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
dataset.drop(['隊伍', '日期', '得分'], inplace=True, axis=1)
y = dataset['勝負'].values
dataset.drop('勝負', inplace=True, axis=1)
X = dataset.values
print(X.shape)


## 將數據集拆成訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

## 訓練與建構迴歸模型
randomForestModel = RandomForestClassifier(max_depth=2, random_state=0)
randomForestModel.fit(X_train, y_train)

score = randomForestModel.score(X_test, y_test)
print('Score: ', score)
print('Accuracy: ' + str(score*100) + '%')
## 拿訓練好的迴歸模型預測測試集資料的目標值(依變數)
y_pred = randomForestModel.predict(X_test)
print('Predict : ', y_pred)
from sklearn import metrics
print(metrics.classification_report(y_test,y_pred))
print('特徵重要程度: ',randomForestModel.feature_importances_)
importances = randomForestModel.feature_importances_
indices = np.argsort(importances)#[::-1]

col_name = dataset.columns

labels = []
gini_im = []
for i in indices[-10:]:
    labels.append(col_name[i])
    gini_im.append(importances[i])
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 改字體，標題才可以是中文
plt.rcParams['figure.dpi'] = 300
plt.barh(labels, gini_im,)
plt.xlabel('gini importance')
plt.title('Top 10th Important Features')
plt.tight_layout()
plt.savefig('important_features.png', transparent = True)
plt.show()