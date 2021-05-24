# [作業]電商如何以A/B Test 驗證新網頁設計有效
# Can eCommerce UX change boost the conversion rate from 0.13 to 0.15?
# 知識點:
# effect size
# sample size for A/B test
# type I error = 0.05 and Power= 0.8
# z-score, confidence interval
# 參考：A/B testing: A step-by-step guide in Python by Renato Fillinich @ medium.com
# 數據 : ab_data.csv from Kaggle
# [作業目標]
# 了解Binomial分布，以及用常態分布求統計解的方法
# 判讀A/B Test 結果
# [作業重點]
# 如何決定最小樣本數
# 如何以Z值，p-Value和信賴區間(Confidence Interval)判斷A/B結果是否顯著
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.stats.api as sms
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil
# Some plot styling preferences
plt.style.use('seaborn-whitegrid')
font = {'family' : 'Helvetica',
        'weight' : 'bold',
        'size'   : 14}
mpl.rc('font', **font)
#求樣本大小
effect_size = sms.proportion_effectsize(0.13, 0.15) # Calculating effect size based on our expected rates
required_n = sms.NormalIndPower().solve_power(
    effect_size,
    power=0.8,
    alpha=0.05,
    ratio=1
)                               # Calculating sample size needed
required_n = ceil(required_n)   # Rounding up to next whole number無條件進位整數
print(required_n)

# 展示實驗資料
df=pd.read_csv('ab_data.csv')
print(df.head())
print(df.info())
df1=pd.crosstab(df['group'], df['landing_page'])
print(df1)
# 偵測重複出現使用者
print(df['user_id'].duplicated().sum())
# session_counts = df['user_id'].value_counts(ascending=False)
# print(session_counts)
# multi_users = session_counts[session_counts > 1].count()
# print(f'There are {multi_users} users that appear multiple times in the dataset')
# 除去重複出現使用者 
# users_to_drop = session_counts[session_counts > 1].index
# df = df[~df['user_id'].isin(users_to_drop)]
# print(f'The updated dataset now has {df.shape[0]} entries')
df.drop_duplicates('user_id', keep = False , inplace = True)
print(df.shape[0])
# 選取 控制組和實驗組各半 4720 * 2 = 9440
control_sample = df[df['group']=='control'].sample(n=required_n, random_state=22)
treatment_sample = df[df['group']=='treatment'].sample(n=required_n, random_state=22)
ab_test = pd.concat([control_sample,treatment_sample],axis=0)
ab_test.reset_index(drop=True, inplace = True)
print(ab_test)
print(ab_test.info())
# 確認 ab_test 控制組實驗組各半
print(ab_test['group'].value_counts())
#計算conversion rate 平均值，標準差，標準誤
# conversion_rates = ab_test.groupby('group')['converted']
# std_p = lambda x: np.std(x, ddof=0)              # Std. deviation of the proportion
# se_p = lambda x: stats.sem(x, ddof=0)            # Std. error of the proportion (std / sqrt(n))
# conversion_rates = conversion_rates.agg([np.mean, std_p, se_p])
# conversion_rates.columns = ['conversion_rate', 'std_deviation', 'std_error']
# conversion_rates=conversion_rates.apply(lambda x : round(x,3))
# print(conversion_rates)

conversion_rates = ab_test.groupby('group').agg({'converted':['mean','std','sem']})
conversion_rates=conversion_rates.apply(lambda x : round(x,3))
print(conversion_rates)

#繪出 conversion rate 棒狀圖
plt.figure(figsize=(8,6))
sns.barplot(x=ab_test['group'], y=ab_test['converted'], ci=False)
plt.ylim(0, 0.17) 
plt.title('Conversion rate by group', pad=20)
plt.xlabel('Group', labelpad=15)
plt.ylabel('Converted(proportion)', labelpad=15)
plt.show()

#以函數計算z_stat, pval, confidence interval
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
control_results = ab_test[ab_test['group']=='control']['converted']
treatment_results = ab_test[ab_test['group']=='treatment']['converted']
n_con = control_results.count()
n_treat = treatment_results.count()
successes = [control_results.sum(), treatment_results.sum()]
print(successes)
nobs = [n_con, n_treat]
print(nobs)
z_stat, pval = proportions_ztest(successes, nobs=nobs)
(lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(successes, nobs=nobs, alpha=0.05)
print('z statistic:{:.2f}'.format(z_stat))
print('p-value:{:.3f}'.format(pval))
print('ci 95%_for control group:[{:.3f},{:.3f}]'.format(lower_con, upper_con))
print('ci 95%_for treatment group:[{:.3f},{:.3f}]'.format(lower_treat, upper_treat))
# 作業：判讀程式最後統計結果，A/B test 是否顯著
print('since alpha was set to 0.05 the p-value = 0.732 which is larger than 0.05 --> cannot reject the null hypothesis (proportion difference between the control and treatment groups are the same)')

# 作業：試以(0.12, 0.11)計算結果是否顯著
# 作業：樣本數是以那些模組/函數算的
#求樣本大小
effect_size = sms.proportion_effectsize(0.12, 0.11) # Calculating effect size based on our expected rates
required_n = sms.NormalIndPower().solve_power(
    effect_size,
    power=0.8,
    alpha=0.05,
    ratio=1
)                               # Calculating sample size needed
required_n = ceil(required_n)   # Rounding up to next whole number無條件進位整數
print(required_n)

# 展示實驗資料
df=pd.read_csv('ab_data.csv')
# 除去重複出現使用者
df.drop_duplicates('user_id', keep = False , inplace = True)
print(df.shape[0])
# 選取 控制組和實驗組各半 15970 * 2 = 31940
control_sample = df[df['group']=='control'].sample(n=required_n, random_state=22)
treatment_sample = df[df['group']=='treatment'].sample(n=required_n, random_state=22)
ab_test = pd.concat([control_sample,treatment_sample],axis=0)
ab_test.reset_index(drop=True, inplace = True)
print(ab_test)
print(ab_test.info())
# 確認 ab_test 控制組實驗組各半
print(ab_test['group'].value_counts())

conversion_rates = ab_test.groupby('group').agg({'converted':['mean','std','sem']})
conversion_rates=conversion_rates.apply(lambda x : round(x,3))
print(conversion_rates)

#繪出 conversion rate 棒狀圖
plt.figure(figsize=(8,6))
sns.barplot(x=ab_test['group'], y=ab_test['converted'], ci=False)
plt.ylim(0.120, 0.1225) 
plt.title('Conversion rate by group', pad=20)
plt.xlabel('Group', labelpad=15)
plt.ylabel('Converted(proportion)', labelpad=15)
plt.show()
#以函數計算z_stat, pval, confidence interval

from statsmodels.stats.proportion import proportions_ztest, proportion_confint
control_results = ab_test[ab_test['group']=='control']['converted']
treatment_results = ab_test[ab_test['group']=='treatment']['converted']
n_con = control_results.count()
n_treat = treatment_results.count()
successes = [control_results.sum(), treatment_results.sum()]
print(successes)
nobs = [n_con, n_treat]
print(nobs)
z_stat, pval = proportions_ztest(successes, nobs=nobs)
(lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(successes, nobs=nobs, alpha=0.05)
print('z statistic:{:.2f}'.format(z_stat))
print('p-value:{:.3f}'.format(pval))
print('ci 95%_for control group:[{:.3f},{:.3f}]'.format(lower_con, upper_con))
print('ci 95%_for treatment group:[{:.3f},{:.3f}]'.format(lower_treat, upper_treat))
# 作業：判讀程式最後統計結果，A/B test 是否顯著
print('Ans : 0.945>0.05,無顯著')

# 作業：樣本數是以那些模組/函數算的
'''Ans：根據https://www.statmethods.net/stats/power.html ， 可從四個變數中的三個（效應值、樣本數量、
Type Ⅰ error水準(預設為0.05)、檢定力(1-Type Ⅱ error)），推導出第四個。因為是反推，需要用到
statsmodels.stats.api(power).NormalIndPower().solve_power(effect_size, power, alpha, ratio)
以及statsmodels.stats.proportion.proportion_effectsize(比例1, 比例2)
而比例1與比例2為變數1與變數2的發生事件比例（代表題目是一個比例檢定）'''