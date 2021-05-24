# 作業說明
# (這是Udacity關於A/B Test的期末專題)
# Udacity希望了解，在免費14天試學網頁上，除了要信用卡資訊外，還想了解學生願意花多少小時學。如果少於某門檻(5小時)，就建議學生不要註冊，免費聽聽影音就好，免得浪費資源，降低學習成功率。
# 我們的題目是，增加這個頁面，是否對Gross Conversion(GC)和Net Conversion (NC)在統計學上(Alpha=0.05，Power=0.8)有幫助(d=0.01/0.0075)，亦即統計上的顯著(Significant)。
# CI = click 數目
# GC = 註冊數/CI (聽了建議仍然註冊的比例)
# NC = 繳費數/CI (14天之後繳費且繼續的比例)
# 我們期待GC比原來下降，但NC不降，這表示省去資源但收入不降。

# 作業目標
# 經由範例程式，學習A/B Test 的步驟
# 最低樣本數的計算方法
# 自行開發信賴區間計算函數

#載入程式庫
import math as mt
import numpy as np
import pandas as pd
from scipy.stats import norm

#將基礎數據放入字典
baseline = {"Cookies":40000,"Clicks":3200,"Enrollments":660,"CTP":0.08,"GConversion":0.20625,
           "Retention":0.53,"NConversion":0.109313}
#調整大小到以Cookie為基準
baseline["Cookies"] = 5000
baseline["Clicks"]=baseline["Clicks"]*(5000/40000)
baseline["Enrollments"]=baseline["Enrollments"]*(5000/40000)
print(baseline)
# 算出 Gross Conversion (GC) 的 p 和 n
# 還有 Stansard Deviation(sd) rounded to 4 decimal digits
GC={}
GC['d_min']=0.01
GC['p']=baseline['GConversion']
#p is given in this case - or we could calculate it from enrollments/clicks
GC['n']=baseline['Clicks']
GC['sd']=round(mt.sqrt((GC['p']*(1-GC['p']))/GC['n']),4)
print(GC['sd'])

# Retention(R) 
R={}
R['d_min']=0.01
R['p']=baseline['Retention']
R['n']=baseline['Enrollments']
R['sd']=round(mt.sqrt((R['p']*(1-R['p']))/R['n']),4)
print(R['sd'])

# Net Conversion (NC)
NC={}
NC['d_min']=0.0075
NC['p']=baseline['NConversion']
NC['n']=baseline['Clicks']
NC['sd']=round(mt.sqrt((NC['p']*(1-NC['p']))/NC['n']),4)
print(NC['sd'])


#計算 Z-score
def get_z_score(alpha):
    return norm.ppf(alpha)

# 得到兩個(A/B)標準差
def get_sds(p,d):
    sd1=mt.sqrt(2*p*(1-p))
    sd2=mt.sqrt(p*(1-p)+(p+d)*(1-(p+d)))
    sds=[sd1,sd2]
    return sds

# 求Sample Size
def get_sampSize(sds,alpha,beta,d):
    n=pow((get_z_score(1-alpha/2)*sds[0]+get_z_score(1-beta)*sds[1]),2)/pow(d,2)
    return n

GC["d"]=0.01
R["d"]=0.01
NC["d"]=0.0075

# Let's get an integer value for simplicity
GC['sampsize']=round(get_sampSize(get_sds(GC['p'],GC['d']),0.05,0.2,GC['d']))
print(GC['sampsize'])
GC['sampsize']=round(GC['sampsize']/0.08*2)
print(GC['sampsize'])
# Getting a nice integer value
R['sampsize']=round(get_sampSize(get_sds(R['p'],R['d']),0.05,0.2,R['d']))
print(R['sampsize'])
R['sampsize']=R['sampsize']/0.08/0.20625*2
print(R['sampsize'])
# Getting a nice integer value
NC['sampsize']=round(get_sampSize(get_sds(NC['p'],NC['d']),0.05,0.2,NC['d']))
print(NC['sampsize'])
NC['sampsize']=NC['sampsize']/0.08*2
print(NC['sampsize'])

# 載入數據
control=pd.read_csv("control_data.csv")
experiment=pd.read_csv("experiment_data.csv")
print(control.head())
pageviews_cont = control['Pageviews'].sum()
pageviews_exp = experiment['Pageviews'].sum()
pageviews_total=pageviews_cont+pageviews_exp
print ("number of pageviews in control:", pageviews_cont)
print ("number of Pageviewsin experiment:" ,pageviews_exp)

# Count the total clicks from complete records only
clicks_cont = control['Clicks'].loc[control['Enrollments'].notnull()].sum()
print(clicks_cont)
clicks_exp = experiment['Clicks'].loc[experiment['Enrollments'].notnull()].sum()
print(clicks_exp)
# Gross Conversion - number of enrollments divided by number of clicks
enrollments_cont=control['Enrollments'].sum()
enrollments_exp=experiment['Enrollments'].sum()
print(enrollments_cont)
print(enrollments_exp)
GC_cont = enrollments_cont/clicks_cont
GC_exp = enrollments_exp/clicks_exp
GC_pooled = (enrollments_cont+enrollments_exp)/(clicks_cont+clicks_exp) #d
GC_sd_pooled = mt.sqrt(GC_pooled*(1-GC_pooled)*(1/clicks_cont+1/clicks_exp))
alpha = 0.05
GC_ME = round(get_z_score(1-alpha/2)*GC_sd_pooled,4)
GC_diff = round(GC_exp-GC_cont,4)
print("The change due to the experiment is",GC_diff*100,"%")
print("Confidence Interval: [",GC_diff-GC_ME,",",GC_diff+GC_ME,"]")
print ("The change is statistically significant if the CI doesn't include 0. In that case, it is practically significant if",-GC["d_min"],"is not in the CI as well.")

#Net Conversion - number of payments divided by number of clicks
payments_cont = control['Payments'].sum()
payments_exp = experiment['Payments'].sum()
print(payments_cont)
print(payments_exp)
NC_cont = payments_cont/clicks_cont
NC_exp = payments_exp/clicks_exp
NC_pooled = (payments_cont+payments_exp)/(clicks_cont+clicks_exp) #d
NC_sd_pooled = mt.sqrt(NC_pooled*(1-NC_pooled)*(1/clicks_cont+1/clicks_exp))
alpha = 0.05
NC_ME = round(get_z_score(1-alpha/2)*NC_sd_pooled,4)
NC_diff = round(NC_exp-NC_cont,4)
print("The change due to the experiment is",NC_diff*100,"%")
print("Confidence Interval: [",NC_diff-NC_ME,",",NC_diff+NC_ME,"]")
print ("The change is statistically significant if the CI doesn't include 0. In that case, it is practically significant if",NC["d_min"],"is not in the CI as well.")

# 作業 嘗試以函數算出樣本數
import statsmodels.stats.api as sms
from math import ceil
print(GC)
# want to know the size for GC with bias = 1* min change which is practical significant.
effect_size = sms.proportion_effectsize(GC['p']-1.0*GC['d_min'],GC['p']+0.0*GC['d_min'])
required_n = sms.NormalIndPower().solve_power(
    effect_size,
    power = 0.8,
    alpha = 0.05,
    ratio = 1
    )
required_n = ceil(required_n)
print(effect_size, required_n)
print('required n of pageviews=',required_n/0.08*2)

# 作業 自行開發雙樣本比例的信賴區間函數
import scipy.stats as stats
def two_proprotions_confint(success_a, size_a, success_b, size_b, significance = 0.05):
    prop_a = success_a / size_a
    prop_b = success_b / size_b
    pooled = (success_a+success_b)/(size_a+size_b)
    sd_pooled = mt.sqrt(pooled*(1-pooled)*(1/size_a+1/size_b))
    # var = prop_a * (1 - prop_a) / size_a + prop_b * (1 - prop_b) / size_b
    # se = np.sqrt(var)
    z = stats.norm.ppf(1 - (significance / 2))
    prop_diff = prop_b - prop_a
    confint = prop_diff + np.array([-1, 1]) * z * sd_pooled
    return prop_diff, confint
print(two_proprotions_confint(enrollments_cont, clicks_cont, enrollments_exp, clicks_exp, significance = 0.05))


    
