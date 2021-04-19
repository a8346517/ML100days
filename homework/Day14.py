import pandas as pd
# HW 讀取資料夾中 boston.csv 讀取其欄位 CHAS、NOX、RM，輸出成.xlsx檔案
pdb = pd.read_csv("boston.csv",usecols=['CHAS','NOX','RM'])
print(pdb)
pdb.to_excel('my boston.xlsx',sheet_name = 'Boston')

#HW1  比較下列兩個讀入的 df 有什麼不同？為什麼造成的？
df1 = pd.read_csv('https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv')
df2 = pd.read_csv(
    'https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv',
    keep_default_na=True,
    na_values=['na', '--']
)
print(df1)
print(df2)

# 把df2的 na,-- 定義為變為NaN

# HW2 請將 Dcard API 取得所有的看板資訊轉換成 DataFrame，並且依照熱門程度排序後存成一個 csv 的檔案。
import requests
r = requests.get('https://www.dcard.tw/_api/forums')
response = r.text

import json
data = json.loads(response)
#print(data)
df = pd.DataFrame(data)
df= df.sort_values(by='subscriptionCount', ascending=False)
print(df)
df.to_csv('decard.csv')