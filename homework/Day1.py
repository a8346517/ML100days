import numpy as np
# 上課內容
a = np.arange(15).reshape(3, 5)
print(a)
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])

print(type(a)) # <type 'numpy.ndarray'>

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)
#ndarray.ndim： 陣列有多少維度
#ndarray.shape： 每個維度的大小
#ndarray.size： 陣列當中有幾個元素
#ndarray.dtype： 陣列中的資料型態
#ndarray.itemsize： 陣列中每個元素佔用的空間
#ndarray.data： 陣列所存在的記憶體位置

print(list(a))
# [array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9]), array([10, 11, 12, 13, 14])]

print(a.tolist())
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

#HW1 list(a), 與 a.tolist()的差異
print('list(a)只會第一層型態轉換為list: ', list(a))
print('tolist()多層型態轉換為list: ', a.tolist())

#HW2 

import numpy as np
a = np.random.randint(10, size=6)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(len(a))
print(type(a))

b = np.random.randint(10, size=(3,4))
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)
print(len(b))
print(type(b))

c = np.random.randint(10, size=(2,3,2)) 
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)
print(c.itemsize)
print(len(c))
print(type(c))

#HW3 如何利用 list(...) 實現 a.tolist() 的效果
a = np.random.randint(10, size=6)
b = np.random.randint(10, size=(3,4))
c = np.random.randint(10, size=(2,3,2))
def tolist(iterable):
    return iterable.tolist()
print(tolist(a))
print(tolist(b))
print(tolist(c))

# 延伸題
a=np.arange(0,21,1)
print(a)
b=np.arange(2,21,2)
print(b)
c=np.arange(3,21,3)
print(c)