# HW1 在速度較慢的時候，可以先從哪邊開始檢查？
print('檢查資料格式(用api去讀取)、盡量使用python內部函式(egg)、用向量化去解(isin)')
import pandas as pd
import numpy as np 
import time
score_df = pd.DataFrame([[1,50,80,70,'boy',1], 
              [2,60,45,50,'boy',2],
              [3,98,43,55,'boy',1],
              [4,70,69,89,'boy',2],
              [5,56,79,60,'girl',1],
              [6,60,68,55,'girl',2],
              [7,45,70,77,'girl',1],
              [8,55,77,76,'girl',2],
              [9,25,57,60,'girl',1],
              [10,88,40,43,'girl',3],
              [11,25,60,45,'boy',3],
              [12,80,60,23,'boy',3],
              [13,20,90,66,'girl',3],
              [14,50,50,50,'girl',3],
              [15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])
start_time= time.time()
score_df.groupby('class').agg('mean')
end_time = time.time()
print(end_time-start_time)

start_time= time.time()
score_df.groupby('class').transform('mean')
end_time = time.time()
print(end_time-start_time)

score_df1 = score_df.copy()
star_time = time.time()
score_df1['Pass_math'] = score_df1.math_score>=60
end_time = time.time()
print(end_time - star_time)

score_df3 = score_df.copy()
star_time = time.time()
score_df3['Pass_math'] = score_df3.math_score.isin(range(60, 100))
end_time = time.time()
print(end_time - star_time)
# HW2 資料過大時應採取什麼方式讓記憶體占用量下降？
print('把欄位的型態降級，有助於減少記憶體佔用空間(float64->float32)')
float_data = pd.DataFrame(np.random.uniform(0,5,100000).reshape(1000,100))
int_data = pd.DataFrame(np.random.randint(0,1000,100000).reshape(1000,100))
print(int_data.memory_usage(deep=True).sum(), float_data.memory_usage(deep=True).sum())

downcast_float = float_data.apply(pd.to_numeric,downcast='float')
print(float_data.memory_usage(deep=True).sum(),downcast_float.memory_usage(deep=True).sum())

compare_float = pd.concat([float_data.dtypes,downcast_float.dtypes],axis=1)
compare_float.columns = ['before','after']
print(compare_float.apply(pd.value_counts))

downcast_int = int_data.apply(pd.to_numeric,downcast='unsigned')
print(int_data.memory_usage(deep=True).sum(),downcast_int.memory_usage(deep=True).sum())
compare_int = pd.concat([int_data.dtypes,downcast_int.dtypes],axis=1)
compare_int.columns = ['before','after']
print(compare_int.apply(pd.value_counts))