import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn  as sns
from scipy import stats
import math
import statistics

df_train = pd.read_csv("Titanic_train.csv")
print(df_train.info()) #Fare無缺失值
g = sns.FacetGrid(df_train,col='Survived')
g.map(sns.distplot, 'Fare', kde = False)
plt.show()
#先透過 計算統計值， 分別呈現數量，年齡平均，標準差，最大值和最小值。
print(df_train['Fare'].describe())


#進行3倍標準差原則的計算，從而檢視哪些值是可疑的異常值。
def out_score(y,times) :
    y_mean = np.mean(y)
    y_std = np.std(y)
    z_score=[]
    for i in y :
        z_score.append((i-y_mean) / y_std)
    return np.where(np.abs(z_score) > times) #np.abs 絕對值
out_index = out_score(df_train['Fare'],3)
print(out_index[0])
print("用第二種方法的找出的 outlier 有哪些?")
print(df_train['Fare'].loc[out_index[0]])
# 異常值的判別方法3-盒鬚圖判別法(IQR method)
def out_iqr(y,times) :
    q1,q3 = np.percentile(y,[25,75])
    iqr = q3 - q1
    low  = q1 - (iqr*times)
    hign = q3 + (iqr*times)
    return np.where((y > hign) | (y < low))
out_index2 = out_iqr(df_train['Fare'],2)
print(out_index2[0])
print("用第二種方法的找出的 outlier 有哪些?")
print(df_train['Fare'].loc[out_index2[0]])
# 畫盒鬚圖
# 使用np.isnana(data)，找出在 age中的遺失值，然後逐位反轉，讓遺失值為 0,則可以透過索引的方式，濾掉遺失值。
plt.boxplot(df_train['Fare'][~np.isnan(df_train['Fare'])],whis=2)    #作圖
plt.title('Box Plot')
plt.show()
# Q2:你覺得找出的異常是真的異常? 你覺得需要做處理嗎?
print("正常,因為就像頭等艙價格一定高於經濟艙很多層次,而且少數人才會做頭等艙,所以不能算異常")