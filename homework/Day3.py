# HW1 請比較 np.zeros 和 np.empty 產生出來的陣列有何差異？為什麼要設計兩種方法？
import numpy as np
print(np.zeros((2, 3))) #可以依照傳入的形狀引數
print(np.empty((2, 3))) #不需要給定起始值，但是可以建立給定形狀的陣列

# HW2 在不用「整數亂數方法」的限制下，如何將包含小數的轉換整數？
a =np.random.rand(2,3)
a=a*100
print(a)
#b = np.array(a,dtype="int32")
b= a.round()
print(b)

# HW3承上題，怎樣可以限制整數的範圍介於 m - n 之間
m=20
n=40
a = np.random.randint(m,n,size=(2,3))
print(a)
b = m+(n-m-1)*np.random.rand(2,3)
print(b.round())

# 進階
dt = np.dtype({'names':('name', 'sex', 'weight','rank', 'myopia'), 'formats':('U10', 'U5',np.float, np.int, np.bool)})
c = np.zeros(8, dtype = dt)
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]
c["name"]=name_list
c["sex"]=sex_list
c["weight"]=weight_list
c["rank"]=rank_list
c["myopia"]=myopia_list
print(c)
print(sum(c['weight']) / c['weight'].size)
boy=np.where(c['sex']=='boy')
print(sum(c['weight'][boy])/c['weight'][boy].size)
girl=np.where(c['sex']=='girl')
print(sum(c['weight'][girl])/c['weight'][girl].size)