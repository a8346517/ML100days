import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display
import sklearn
from sklearn.feature_selection import VarianceThreshold
from sklearn import preprocessing
from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE
from sklearn.svm import SVC
df_train = pd.read_csv("Titanic_train.csv")
print(df_train.info())
#1.產稱一個新的變數 Survived_cate ，資料型態傳換成類別型態      
#2.把題目中的 Survived 用 Survived_cate 來做分析    

df_train['Survived_cate']=df_train['Survived'].astype('object')
print(df_train.info())
# 我們先把遺失值刪除
# 取出資料後，把遺失值刪除
complete_data=df_train.dropna()
#排除 Ｎame 當特徵，先刪除每一個人都是獨特的資料，先檢視其他變數
complete_data=complete_data.drop(['Name','Ticket','PassengerId'], axis=1)
print(complete_data.head(5))
print(complete_data.shape)
num_features = []
for dtype, feature in zip(complete_data.dtypes, complete_data.columns):
    if dtype == 'float64' or dtype == 'int64':
        num_features.append(feature)
print(f'{len(num_features)} Numeric Features : {num_features}\n')
cat_features = []
for dtype, feature in zip(complete_data.dtypes, complete_data.columns):
    if dtype == 'object':
        cat_features.append(feature)
print(f'{len(cat_features)} category Features : {cat_features}\n')
x=complete_data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare','Sex', 'Embarked']]
y=complete_data['Survived']
print(x.head(5))
print(y.head(5))
# Q1: 目標變數為 Survived，試著用今天教授的包裝法，搭配課程所教的 SVC，試著排出其餘特徵的重要性!
sex = {'male':1,'female':0}
complete_data['Sex1'] = complete_data['Sex'].map(sex)
embarked = pd.get_dummies(complete_data[["Embarked"]])
print(embarked)
complete_data = pd.concat([complete_data,embarked],axis=1)
print(complete_data)
x=complete_data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare','Sex1', 'Embarked_C','Embarked_Q','Embarked_S']]
y=complete_data['Survived']
print(x.head(5))
estimator = SVC(kernel='linear')
selector = RFE(estimator,n_features_to_select = 2, step=1)
selector = selector.fit(x,y)
print(selector.support_)
ranking = selector.ranking_
print(ranking)
rfe_feature = x.loc[:,selector.support_].columns.tolist()
print("與生存率有關聯的2個關鍵是:",rfe_feature)
