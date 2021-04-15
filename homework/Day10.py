#HW1 請問下列四種不同的 DataFrame 選取結果有什麼差異？
import pandas as pd
# df.loc[ '2013-01-01', 'A'] 取出 '2013-01-01'列的 'A'欄資料值
# df.loc[ '2013-01-01', ['A', 'B'] ] 取出 '2013-01-01'列的 'A','B'欄資料值
# df.loc[ '2013-01-01':'2013-01-02', 'A' ] 取出 '2013-01-01'到 '2013-01-02'列的 'A'欄資料值
# df.loc[ '2013-01-01':'2013-01-05', 'A':'C'] 取出 '2013-01-01'到'2013-01-05'列的 'A'到'C'欄資料值

#HW2 請根據提供的資料，選擇出下列的要求：
# - select the first 3 rows.
# - select the odd rows. (index = 1, 3, 5)
# - select the last 2 columns.
# - select the even columns. (index = 0, 2, 4)
import numpy as np
df = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df[0:3])
print(df[df.index%2==1])
print(df.iloc[:,-2:])
print(df.iloc[0::2])

#HW3 請根據提供的資料，選擇出下列的要求：
# - 1. filtered by first column > 20?
# - 2. filtered by first column + second column > 50
# - 3. filtered by first column < 30 or second column > 30
# - 4. filtered by total sum of row > 100

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df[df[0]>20])
print(df[df[0]+df[1]>50])
print(df[(df[0]<30) | (df[1]>30)])
print(df[df.sum(axis=1)>100])

#進階
A = pd.read_csv("STOCK_DAY_0050_202009.csv")
B = pd.read_csv("STOCK_DAY_0050_202010.csv")
print(A.head(5))
print(B.head(5))
C=pd.concat([A,B],axis=0).reset_index(drop=True)
print(C)
print(C[C['open']<C['close']])