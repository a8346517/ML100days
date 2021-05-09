import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
data = pd.read_csv("Titanic_train.csv")
# step1: 觀察 Age 和 Pclass 與 Sex 是否有關連性?
# step2: 如果有關連性，運用 KNN ，取出 Age 、 Pclass、 Sex的資料，以 Sex 與 Pclass 補 Age 遺失值。
print(data.head())
#計算每一行是否有遺失值，計算遺失比例
missing_vals = data.isnull().sum()/len(data)
print(missing_vals)
missing_vals.sort_values(ascending=False)
missing_vals = pd.DataFrame(missing_vals,columns=['missing_rate'])
print(missing_vals)

# 觀察資料
# 性別和年紀的關係
g = sns.boxplot(x="Pclass", y="Age", hue="Sex",
               data=data)
plt.show()


# #男生女生個數
g = sns.catplot("Sex",data=data,kind="count", height=2.5, aspect=.8)
plt.show()

# #男生女生中年齡分布
g = sns.catplot("Sex",'Age',data=data,kind="box", height=2.5, aspect=.8)
plt.show()

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
data['Sex']= le.fit_transform(data['Sex'])
print(data['Sex'])
data = data[['Pclass','Sex','Age']]
from sklearn.metrics.pairwise import nan_euclidean_distances
print(pd.DataFrame(nan_euclidean_distances(data)))

k = 5
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=k, add_indicator = True, weights = 'uniform')
df_filled = pd.DataFrame(imputer.fit_transform(data))
print(df_filled)
print(df_filled.isnull().any()) # 檢察都沒有遺失值
df_filled.rename(columns={0:'Pclass', 1:'Sex', 2:'Age',3:'imputer.Age'}, inplace = True)
sns.boxplot(x='Pclass', y='Age',hue='Sex', data=df_filled)
plt.show()

# sex 類別- 類別資料轉換對於 KNN 的影響
data = pd.read_csv("Titanic_train.csv")
data['Sex'].replace({'male':0, 'female':1000},inplace = True)
data = data[['Pclass','Sex','Age']]
K=5
imputer = KNNImputer(n_neighbors = K, add_indicator = True, weights = 'uniform')
df_filled = pd.DataFrame(imputer.fit_transform(data))
print(df_filled)
df_filled.rename(columns={0:'Pclass', 1:'Sex', 2:'Age',3:'imputer.Age'}, inplace = True)
sns.boxplot(x='Pclass', y='Age',hue='Sex', data=df_filled)
plt.show()


# 判斷補值的好壞?
# Step1:取無遺失值的資料集
# Step2:隨機取幾個資料點，當作遺失值
# Step3:以step2產生的遺失值進行補值
# Step4: 計算MSE看補值的效果。
data = pd.read_csv("Titanic_train.csv")
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
data['Sex']= le.fit_transform(data['Sex'])
print(data['Sex'])
data = data[['Pclass','Sex','Age']]

# Step1:取無遺失值的資料集
import random
completet_data = data.dropna()
completet_data = completet_data.reset_index(drop=True)
print(completet_data)
# Step2:隨機取幾個資料點，當作遺失值
a = random.sample(list(completet_data.index),10)
miss_data = completet_data.copy()
miss_data['Age'].iloc[a] = np.nan
# Step3:以step2產生的遺失值進行補值
k = 5
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=k, add_indicator = True, weights = 'uniform')
verify_impute = pd.DataFrame(imputer.fit_transform(miss_data))
verify_impute.rename(columns={0:'Pclass', 1:'Sex', 2:'Age',3:'imputer.Age'}, inplace = True)
print(verify_impute)
# 判斷 df_filled 和 data 的距離
# Step4: 計算MSE看補值的效果。
from sklearn.metrics import mean_squared_error
y1 = completet_data['Age']
y2 = verify_impute['Age'] 
MSE_h = mean_squared_error(y1,y2)
print(MSE_h)