# HW1 將所有轉為周資料
import numpy as np
import pandas as pd
index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)
print(series)
series1=series.to_period('w')
print(series1)


#HW2 將周資料的值取平均
print(series.resample("w").mean())