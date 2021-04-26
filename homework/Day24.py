# # 導入必要的程式庫
# import pandas as pd
# import seaborn as sns
# from matplotlib import pyplot as plt

# # 取得鳶尾花資料集
# df = sns.load_dataset('iris')
# df.info()
# sns.boxplot(data = df,orient='h')
# plt.show()

# sns.stripplot(x = "species", y = "petal_length", data = df)
# plt.show()

# sns.stripplot(x = "species", y = "petal_length", data = df, jitter=True)
# plt.show()

# #可以調整jitter 參數讓分布更清晰
# sns.stripplot(x = "species", y = "petal_length", data = df, jitter=0.3)
# plt.show()

# # 可以換個方向, 交換 x/y
# sns.stripplot(x = "petal_length", y = "species", data=df, jitter=True)
# plt.show()

# # dodge : True / False, 若設置為True則沿著分類軸，將數據分離出來
# sns.stripplot(x = "petal_length", y = "species", data=df, dodge=True)
# plt.show()

#HW1
# 導入必要的程式庫
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得資料集
df = sns.load_dataset('titanic')
df.info()
# 選取特徵值: sex, survived, 主要是這個資料集用來做存活率做預測, 所以Y label 一定是用survived
ax = sns.barplot(x="sex", y="survived",hue='class', data=df)
plt.show()

#HW2

# 取得資料集
df = sns.load_dataset('tips')
df.info()

sns.boxplot(x='sex',y='tip', data=df)
sns.stripplot(x='sex', y='tip',jitter=0.3,data=df)
plt.show()