# HW1 根據題目給的 DataFrame 完成下列操作：
#- 計算每個不同種類 animal 的 age 的平均數
#- 計算每個不同種類 animal 的 age 的平均數
#- 將資料依照 Age 欄位由小到大排序，再依照 visits 欄位由大到小排序
#- 將 priority 欄位中的 yes 和 no 字串，換成是布林值 的 True 和 False
import pandas as pd
import numpy as np
data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
print(df)
print(df[df['animal']=='cat'].age.mean())
print(df[df['animal']=='snake'].age.mean())
print(df[df['animal']=='dog'].age.mean())
df1=df.sort_values(by=['age'])
df2=df1.sort_values(by=['visits'],ascending=False)
print(df2)
df['priority']=df['priority'].str.replace('yes','True')
df['priority']=df['priority'].str.replace('no','False')
print(df)
# HW2  一個包含兩個欄位的 DataFrame，將每個數字減去
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
print(df.apply(lambda i : i-i.mean(axis=0)))
print(df.apply(lambda i : i-df.mean(axis=1)))

# 哪一比的資料總合最小
print(df.sum(axis=0).argmin())
# 哪一欄位的資料總合最小
print(df.sum(axis=1).argmin())

# 進階
#6號學生(student_id=6)3科平均分數為何?
#6號學生3科平均分數是否有贏過班上一半的同學?
#由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問6號同學3科成績分別是?
#承上題，加分後各科班平均變多少?
import pandas as pd
score_df = pd.DataFrame([[1,56,66,70], 
              [2,90,45,34],
              [3,45,32,55],
              [4,70,77,89],
              [5,56,80,70],
              [6,60,54,55],
              [7,45,70,79],
              [8,34,77,76],
              [9,25,87,60],
              [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
score_df = score_df.set_index('student_id')
print(score_df)
print(score_df.mean(axis=1)[5:6])
x=score_df.mean(axis=1)
print(x[6])
if x[6]>score_df.mean(axis=1).median() :
    print('yes')
else :
    print('no')
print(score_df.apply(lambda x: x**(0.5)*10))
x=score_df.apply(lambda x: x**(0.5)*10)
print(x[5:6])
print(x.mean())
