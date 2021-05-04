# Q1:計算標準常態分配，小於1的機率有多大?
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
mu=0
sigma=1
x=np.linspace(-10, 10, 500)
cumsum_probs = stats.norm.cdf(1,mu, sigma)
print("小於1的機率"cumsum_probs)
probs = stats.norm.pdf(x,mu,sigma)
plt.plot(x,probs)
plt.show()
# Q2:計算標準常態分配，大於1，小於 -1 的機率有多大?
cumsum_probs = stats.norm.cdf(-1,mu,sigma)
print("大於1,小於-1的機率",2*cumsum_probs)
#Q3：X~N(2,4),x 服從常態分配，平均數為2,變異數為 4
#，計算 X小於 6 的機率有多大?
mu=2
sigma=4**(1/2)
x = np.linspace(stats.norm.ppf(0.01,mu,sigma),
                stats.norm.ppf(0.99,mu,sigma),500)
print(x)
cumsum_probs = stats.norm.cdf(6,mu,sigma)
print("小於6的機率",cumsum_probs)
probs = stats.norm.pdf(x,mu,sigma)
plt.plot(x,probs)
plt.show()