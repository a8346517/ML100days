import numpy as np 
# HW1  產生一個 1-11 的一維陣列，並且把 3-6 由正數變成負數。
a=np.arange(1,12)
b=[]
for i in a :
    if i>=3 and i<=6 :
        b.append(i*-1)
    else :
        b.append(i)
print(b)

# HW2 試著從一個隨機陣列中，找出比 0.5 大的數有幾個？
A = np.random.rand(3,6)
x=A>0.5
B = A[x]
print(B)
print(B.size)
# 進階
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])
print('英文平均分數:',english_score.mean(),'最高分:',english_score.max(),'最低分:',english_score.min(),'標準差:',english_score.std())
print('數學平均分數:',np.nanmean(math_score),'最高分:',np.nanmax(math_score),'最低分:',np.nanmin(math_score),'標準差:',np.nanstd(math_score))
print('國文平均分數:',chinese_score.mean(),'最高分:',chinese_score.max(),'最低分:',chinese_score.min(),'標準差:',chinese_score.std())

math_score[4] = 55
print('數學平均分數:',math_score.mean(),'最高分:',math_score.max(),'最低分:',math_score.min(),'標準差:',math_score.std())

a = np.corrcoef([chinese_score,english_score])
b = np.corrcoef([chinese_score,math_score])
print(a,b) # 跟英文相似度較高