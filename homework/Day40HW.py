import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display
import sklearn
import pingouin as pg
import researchpy 
df_train = pd.read_csv("Titanic_train.csv")
print(df_train.info())
df_train['Survived_cate'] = df_train['Survived'].astype('object')
data = df_train[['Age','Survived_cate','Sex']].dropna()
print(data)
# Q1: 產生一個新的變數(Age_above65_) Age>=65為 'Y'，其餘為'N'。
def age_map(x):
    if x>=65:
        return('Y')
    else :
        return('N')
data['Age_above65_']=data['Age'].apply(age_map)
print(data)
# Q2: 添加女性和男性，產生一個新的變數(Age_above65_female)，女性或Age>=65為'Y'，其餘為'N'。
def age_map2(x):
    if x.Sex == 'female':
        return("Y")
    else:  
        if x.Age>=65 :
           return("Y")
        else:
            return("N")

data['Age_above65_female']=data.apply(age_map2, axis=1)
print(data)
# Q3: 透過昨天課程的內容，驗證產生的兩個新變數，哪一個和目標變數(Survived_cate)的相關性較高?
#離散VS離散
contTable = pd.crosstab(data['Age_above65_'],data['Survived_cate'])
contTable1 = pd.crosstab(data['Age_above65_female'],data['Survived_cate'])
print(contTable)
print(contTable1)
df = min(contTable.shape[0],contTable.shape[1])-1
df1 = min(contTable1.shape[0],contTable1.shape[1])-1
print(df)
print(df1)
crosstab,res = researchpy.crosstab(data['Age_above65_'],data['Survived_cate'],test='chi-square')
crosstab1,res1 = researchpy.crosstab(data['Age_above65_female'],data['Survived_cate'],test='chi-square')
print(res)
print(res1)
print(res.loc[2,'results'])
print(res1.loc[2,'results'])
def judgment_etaSq(x):
    if x < 0.10:
        qual = 'negligible'
    elif x < 0.30:
        qual = 'small'
    elif x < 0.50:
         qual = 'medium'
    else:
        qual = 'large'
    return(qual)
print(judgment_etaSq(res.loc[2,'results']))
print(judgment_etaSq(res1.loc[2,'results']))
print("由此可知Age_above65_female有很大的相關")

g = sns.countplot(x='Age_above65_',hue='Survived_cate',data = data)
plt.show()
g = sns.countplot(x='Age_above65_female',hue='Survived_cate',data = data)
plt.show()