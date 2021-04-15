#HW1 請建立類似提供結果的 DataFrame
#    Apples  Bananas
# 0      30       21
import pandas as pd
df = pd.DataFrame({'Apples': [30] ,
                   'Bananas' : [21] })
print(df)

#             Apples  Bananas
# 2017 Sales      35       21
# 2018 Sales      41       34
df = pd.DataFrame({'Apples': [35,41] ,
                   'Bananas' : [21,34] },index=['2017 Sales','2018 Sales'])
print(df)

# HW2 請問如果現在有一個 DataFrame 如下，請問資料在 Python 中可能長怎樣？
#      city  visitor weekday
# 0  Austin      139     Sun
# 1  Dallas      237     Sun
# 2  Austin      326     Mon
# 3  Dallas      456     Mon
df1 = pd.DataFrame({'city':['Austin','Dallas','Austin','Dallas'],
                    'visitor':[139,237,326,456],
                    'weekday':['Sun','Sun','Mon','Mon']
})
print(df1)
df2 = pd.DataFrame([['Austin',139,'Sun'],['Dallas',237,'Sun'],['Austin',326,'Mon'],['Dallas',456,'Mon']],
                    columns=['city','visitor','weekday'])
print(df2)
print(df1[df1.weekday=='Sun']['visitor'].mean())
Mon=df2['weekday']=='Mon'
print(df2['visitor'][Mon].mean())


