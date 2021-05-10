import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display

import pingouin as pg
import researchpy
df_train = pd.read_csv("Titanic_train.csv")
print(df_train.info())   
# 產生一個新的變數 Survived_cate ，資料型態傳換成類別型態
df_train['Survived_cate'] = df_train['Survived'].astype('object')
print(df_train.info())
# Q1: 透過數值法計算 Age 和 Survived 是否有相關性?
# 離散 vs 連續 Eta Squared(η2)
#年齡是連續型，生存變數是離散型，故使用eta square 用anova可以找出
#在計算相關性時，不允許有NAN，要先進行補植或刪除
data = df_train[['Age','Survived_cate']].dropna()
print(data)
aov = pg.anova(dv='Age',between = 'Survived_cate',data = data, detailed=True)
print(aov)
etaSq = aov.SS[0]/(aov.SS[0]+aov.SS[1])
print(etaSq)
def judgment_etaSq(x):
    if x < 0.01 :
        a = 'Negligible'
    elif x < 0.06 :
        a = 'small'
    elif x < 0.14 :
        a = 'medium'
    else :
        a = 'large'
    return(a)
print(judgment_etaSq(etaSq))
print('年紀與存活率沒什麼相關性')
g = sns.catplot(x='Survived_cate', y='Age',hue='Survived_cate', data = data, kind = 'violin')
plt.show()    

# Q2:透過數值法計算 Sex 和 Survived 是否有相關性?
# 離散 vs 離散
# step1: 用交叉列連表(contingency table)，來整理兩個類別型的資料
contTable = pd.crosstab(df_train['Sex'],df_train['Survived_cate'])
print(contTable)
df = min(contTable.shape[0],contTable.shape[1])-1
print(df)
crosstab,res = researchpy.crosstab(df_train['Sex'],df_train['Survived_cate'],test = 'chi-square')
print(res)
print("Cramer values : ",res.loc[2,'results'])
def judgment_etaSq(df,V) :
    if df == 1:
        if V < 0.10:
            qual = 'negligible'
        elif V < 0.30:
            qual = 'small'
        elif V < 0.50:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 2:
        if V < 0.07:
            qual = 'negligible'
        elif V < 0.21:
            qual = 'small'
        elif V < 0.35:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 3:
        if V < 0.06:
            qual = 'negligible'
        elif V < 0.17:
            qual = 'small'
        elif V < 0.29:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 4:
        if V < 0.05:
            qual = 'negligible'
        elif V < 0.15:
            qual = 'small'
        elif V < 0.25:
            qual = 'medium'
        else:
            qual = 'large'
    else:
        if V < 0.05:
            qual = 'negligible'
        elif V < 0.13:
            qual = 'small'
        elif V < 0.22:
            qual = 'medium'
        else:
            qual = 'large'
    return(qual)
print(judgment_etaSq(df,res.loc[2,'results']))
print("性別與生存率有很大的關係")
g = sns.countplot(x='Sex',hue='Survived_cate', data = df_train)
plt.show()
#由上圖可知女性的生存率比較高

# Q3: 透過數值法計算 Age 和 Fare 是否有相關性?
# 連續vs連續 透過pearsonr方法
data = df_train[['Age','Fare']].dropna()
print(data.info())
corr, _ = stats.pearsonr(data['Age'],data['Fare'])
print(corr)
print("無線性相關")
g = sns.regplot(x='Age', y='Fare',data=data, color='g')
plt.show()