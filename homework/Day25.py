# 載入相關的程式庫
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
df_red = pd.read_csv("winequality_red.csv")
df_white = pd.read_csv("winequality_white.csv")

df_red['color'] = 'r'
df_white['color'] = 'w'
df_all=pd.concat([df_red,df_white],axis=0)
print(df_all.head())

df = pd.get_dummies(df_all, columns=["color"]) #處理缺失值
df_all.isnull().sum()
df_all.info()

df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False) #避免重疊  
plt.tight_layout(rect=(0, 0, 1.2, 1.2))
#作業(1):更改df_all.hist裡面bins的參數值, 看看資料分布的變化
#作業(2):延伸 作業(1), 更改df_all.hist裡面grid的參數值, 看看版面的變化, gird = True
#作業(3):更改 plt.tight_layout(rect=(x1, y1, x2, y2))
df_all.hist(bins=20, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=True) # 資料變成20條直方圖,有網狀方格
plt.tight_layout(rect=(0, 0, 2, 2)) #設定最外框變大            
plt.show()

# #建立一個Figure（空的顯示區）
# fig = plt.figure()

# #直接製圖在剛剛建立的figure
# ax1 = plt.subplot(221)
# ax2 = plt.subplot(223)
# ax3 = plt.subplot(122)

# #避免多個圖重疊，使用tight_layout分開, 可以節省新增Figure的軸的動作
# plt.tight_layout()
# plt.show()

# # Plot multiple seaborn histogram in single graph
# plt.figure(figsize=(7,5))
# sns.histplot(df_all["quality"], bins=10, label="quality")
# sns.histplot(df_all["pH"], bins=10, label="pH")
# sns.histplot(df_all["alcohol"], bins=10, label = "alcohol")
# plt.show()

# df_all.boxplot(column=['volatile acidity','pH','quality'], color='#556270')    
# plt.tight_layout(rect=(0, 0, 1.2, 1.2))
# plt.show()

# sns.heatmap(df_all.corr(),annot = True)
# plt.show()

# # 這個資料集包括了平均數, 標準差, 一定區間的數值
# # 所以, 我們可以考慮使用 bootstrap 幫忙繪製圖表包含 mean, median and mid-range statistics.
# s = pd.Series(df_all['quality'])
# pd.plotting.bootstrap_plot(s, samples=500)
# plt.tight_layout()
# plt.show()