import matplotlib.pyplot as plt
import numpy as np
# x = np.arange(0,180)
# y = np.sin(x * np.pi / 180.0)
# plt.plot(x,y) 
# plt.xlim(-30,390)
# plt.ylim(-1.5,1.5)
# plt.xlabel("x-axis") 
# plt.ylabel("y-axis") 
# plt.title("The Title") 
# plt.show()

# X = np.random.normal(0, 1, 100)
# Y = np.random.normal(0, 1, 100)
# plt.scatter(X,Y)
# plt.title('scatter plot')
# plt.show()
# x = np.arange(0., 10., 0.7)
# y = np.arange(0., 10., 0.7)
# plt.bar(x, y)

# plt.show()

#HW1 畫出 cos 圖檔，並儲存
x = np.arange(0,3*np.pi,0.1)
y_cos = np.cos(x)
plt.plot(x,y_cos)
plt.show()

#HW2 給定散點圖顏色
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)
plt.scatter(X,Y,s=65,c=T,alpha=0.5)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

plt.show()

# 進階 將資料夾中boston.csv讀進來，並用圖表分析欄位。
import pandas as pd
boston = pd.read_csv('boston.csv')
#.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
boston.boxplot()
plt.show()
#.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
boston.plot.scatter(x=['NOX'], y=['DIS'] )
plt.show()

corr=boston[['NOX','DIS']].corr(method = 'pearson')
print(corr,'\n負相關')