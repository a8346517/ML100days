import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
# 某工廠想知道兩條不同的生產線的產品不良率是否有所不同，
# 由兩條生產線中各抽取 300 個樣本，第一組有 75 個不良品，
# 第二組有 30 個不良品，我們可以宣稱生產線所生產出的產品不良率不相同? 
# (以 0.05 為顯著水準)?
# (提示:透過課程投影片的步驟，需思考 𝐻_0、 𝐻_1 的寫法和範例不同唷。)
# H0產出良率相同 pa(75/300)=pb(30/300)
# H1產生良率不相同 pa(75/300) !=pb (30/300)
# 雙尾檢定
import statsmodels.stats.proportion
A = [75,30]
B = [300,300]
X = statsmodels.stats.proportion.proportions_ztest(A,B,alternative = "two-sided")
print(X)
print("p小於0.05 為顯著拒絕H0假設,可以說產品不良率不同")

# 作業 2：你的工作，有需要 A/B test 幫你做決定？
# 可以在論壇中，寫出你的問題，嘗試用今天課程教的方法，
# 透過 5個步驟的拆解，計算出結果，透過統計輔助你做決策。
# 有一個切割機台今天產生良品9000個,總投入量為9300,
# 昨天產生良品為8600,總投入量為8800,我們可以宣稱今天良率大於昨天嗎
# H0 今天良率比昨天高(pa-pb>0) : H1 今天良率沒比昨天高(pa-pb<0)
A = [9000,8600]
B = [9300,8800]
X = statsmodels.stats.proportion.proportions_ztest(A,B,alternative = "smaller")
print(X)
print("p小於0.05 為顯著拒絕H0假設,可以說昨天良率比今天高")