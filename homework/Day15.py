import pandas as pd
import matplotlib.pyplot as plt
# 題目 : 將資料夾中boston.csv讀進來，並用圖表分析欄位。
# HW1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
boston = pd.read_csv('boston.csv')
print(boston.median())
boston.boxplot()
print('TAX')


# 畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係？
boston.plot.scatter(x='NOX',y='DIS')
df_corr = boston[['NOX', 'DIS']].corr(method = 'pearson')
print(df_corr,'\n負相關')
plt.show()
