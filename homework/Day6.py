import numpy as np
# HW1
a= np.arange(6)
print(a)
print(a.sum())
print(np.sum(a))
print(sum(a))
# a.sum() , np.sum(a) 回傳所有加總的值
# sum(a) 回傳軸的加總後的陣列

# HW2 請對一個 5x5 的隨機矩陣作正規化的操作。
A = np.random.random((5,5))
print(A)
B = (A-A.min())/(A.max()-A.min())
print(B)

#HW3 請建立一個長度等於 10 的正整數向量，並且將其中的最大值改成 -1。
c = np.random.randint(1,100,10)
c[c.argmax()] = -1
print(c)

# 進階 將下列陣列(array1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F"),呈上題的array，找出被6除餘1的數的索引
array = np.array(range(30))
array = array.reshape(5,6,order='F')
print(array)
x=np.where(array%6==1)
print(x)
print(array[x])