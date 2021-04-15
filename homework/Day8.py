# HW1  請問 Pandas 套件最主要的貢獻是什麼？
# 對於資料格式有高度的銜接性，包含 CSV、Excel 或資料庫（SQL）皆能提供彈性的讀寫工具

# HW2  根據提供的資料集，印出他們的屬性分別為何？（屬性：shape、size、values、index、columns、dtypes、len）
import pandas as pd 
df = pd.read_csv('https://raw.githubusercontent.com/MachineLearningLiuMing/scikit-learn-primer-guide/master/Data.csv')
print(df)
print(df.shape)
print(df.size)
print(df.values)
print(df.index)
print(df.columns)
print(df.dtypes)
print(len(df))

# 進階
import numpy as np
dt = np.dtype({'names':('name', 'sex', 'weight','rank', 'myopia'), 'formats':('U10', 'U5',np.float, np.int, np.bool)})
array = np.zeros(8, dtype = dt)
print(array)
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]
array['name']=name_list
array['sex']=sex_list
array['weight']=weight_list
array['rank']=rank_list
array['myopia']=myopia_list
print(array['weight'])
print(array['weight'].mean())
print(sum(array['weight'])/array['weight'].size)
boy=np.where(array['sex']=='boy')
print(sum(array['weight'][boy])/array['weight'][boy].size)
print(array['weight'][boy].mean())
girl = np.where(array['sex']=='girl')
print(sum(array['weight'][girl])/array['weight'][girl].size)
print(array['weight'][girl].mean())