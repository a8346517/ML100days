# 丟一個銅板，丟了100次，出現正面 50 次的機率有多大。
# (提示: 先想是哪一種分配，然後透過 python 語法進行計算)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
#二項次分配
n=100
p=0.5
x=50
probs = stats.binom.pmf(x,n,p)
print('出現正面50次機率=',probs)



# low=0
# high=2
# r=np.arange(low,high)

# print(r)
# print(type(r))
# probs = stats.randint.pmf(r,low,high)
# print(probs)
# plt.xlabel("x")
# plt.ylabel("P(X=x)")
# plt.title('0=-,1=+')
# plt.bar(r,probs)
# plt.show()

# cumsum_probs = stats.randint.cdf(r,low,high)
# print(cumsum_probs)
# plt.plot(r,cumsum_probs)
# plt.show()

# k = stats.randint.ppf(cumsum_probs,low,high)
# print(k)

# X = stats.randint.rvs(low,high,size=100)
# print(X)
# plt.hist(X)
# plt.show()

# stat_randint = stats.randint.stats(low,high,moments='mvks')
# print(stat_randint)
# print('randint mean=',stat_randint[0])
# print('randint variance=',stat_randint[1])
# print('randint kurtosis=',stat_randint[2])
# print('randint skew=',stat_randint[3])

# p=0.5
# probs = stats.bernoulli.pmf(r,p)
# print(probs)
# plt.bar(r,probs)
# plt.show()

# cumsum_probs = stats.bernoulli.cdf(r,p)
# print(cumsum_probs)
# plt.plot(r,cumsum_probs)
# plt.show()

# k = stats.bernoulli.ppf(cumsum_probs,p)
# print(k)

# X = stats.bernoulli.rvs(p,size=100)
# print(X)
# plt.hist(X)
# plt.show()

# stats_bernoulli = stats.bernoulli.stats(p,moments='mvks')
# print(stats_bernoulli)
# print('bernoulli mean=',stats_bernoulli[0])
# print('bernoulli variance=',stats_bernoulli[1])
# print('bernoulli kurtosis=',stats_bernoulli[2])
# print('bernoulli skew=',stats_bernoulli[3])


