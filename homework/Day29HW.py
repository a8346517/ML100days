
import matplotlib.pyplot as plt
from scipy.stats import nbinom
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
#Q1: 大樂透的頭獎，你必須從49個挑選出 6 個號碼，
#且這六個號碼與頭獎的六個號碼一致，頭獎的機率是屬於哪一種分配?
print('超幾何分配')
# Q2: 運用範例的 python 程式碼，計算大樂透的中頭獎機率?
lotto = stats.hypergeom.pmf(6,49,6,6)
print(lotto)

# Q3: 你覺得電腦簽注的中獎機率，和人腦簽注相比，哪一個機率高?
print('一樣高')
r = np.arange(0,7)
probs = stats.hypergeom.pmf(r,49,6,6)
print(probs)
plt.bar(r,probs)
plt.show()
cumsum_probs = stats.hypergeom.cdf(r,49,6,6)
print(cumsum_probs)
plt.plot(r,cumsum_probs)
plt.show()
x = stats.hypergeom.ppf(cumsum_probs,49,6,6)
print(x)

s = stats.hypergeom.rvs(49,6,6,size=20)
print(s)
plt.hist(s)
plt.show()

stat_hypergeom = stats.hypergeom.stats(49,6,6,moments='mvks')
print(stat_hypergeom)
