#HW1 請比較對一個 100 x 100 x 100 的陣列，使用不同方法對每一個元素 +1 的時間比較。
import numpy as np
import timeit 
Z = np.random.randint(0,10,1000000).reshape(100,100,100)
# % timeit -n 10 a = 2
Z = Z+1
print(Z)
#flat
Z2=[]
for i in Z.flat :
    Z2.append(i+1)
Z2=np.array(Z2).reshape(100,100,100)
print(Z2)

# nditer
Z3=[]
for i in np.nditer(Z,order='C'):
    Z3.append(i+1)
Z3 = np.array(Z3).reshape(100,100,100)
print(Z3)

# HW2 如何從一個陣列中，找出出現頻率最高的數值與位置？
Z = np.random.randint(0,10,50)
print(Z)
Z1 = np.bincount(Z).argmax()
print("最多出現的數值:",Z1)
Z2 = np.array(np.where(Z==Z1))
print('最多出現的位置:',Z2)

# HW3 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作
a = np.random.randint(10, size=6) 

print(a.tolist())
print(list(a))
x1=[]
for i in list(a):
    x1.append(i)
print(x1)    


b = np.random.randint(10, size=(3,4)) 

print(b.tolist())
print(list(b))
x2=[]
for i in list(b):
    x2.append(list(i))
print(x2)


c = np.random.randint(10, size=(2,3,2)) 

print(c.tolist())
print(list(c))
x3=[]
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        x3.append(list(c[i][j]))
print(x3)

# 進階
array1 = np.array([[10, 8], [3, 5]])
array2 = np.linalg.inv(array1)
print(array2)
print(np.matmul(array1, array2))
print(np.matmul(array2, array1))
print(array1 @ array2)
print(array2 @ array1)

w, v = np.linalg.eig(array1)
print(w)
print(v)

x,y,z = np.linalg.svd(array1)
print(x)
print(y)
print(z)