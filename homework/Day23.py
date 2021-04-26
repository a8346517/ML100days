import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#HW1 顯示的四個變量中, 把hue 套用 sex
# 載入數據集
tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")
print(tips.head())
sns.relplot(x="total_bill", y="tip", hue="sex", style="time",data=tips)
plt.show()

print(fmri.head())
sns.relplot(x="timepoint", y="signal", hue="event", style="region",data=fmri)
plt.show()
sns.regplot(x="timepoint", y="signal",data=fmri)
plt.show()