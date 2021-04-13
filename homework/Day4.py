import numpy as np
# HW1 請問下列程式碼，運算結果分別為何？
a = np.array( [20,30,40,50] )
b = np.array( [1,2,3,4] ) 
c = 1
d = np.array( [1] )
e = np.array( [1,2] ) 
print(a + a) #[40,60,80,100]
print(a + b) #[21,32,43,54]
print(a + c) #[21,31,41,51]
print(a + d) #[21,31,41,51]
#print(a + e) # 錯誤,陣列數要相同
# HW2 如何在不用迴圈的情況下計算 (A+B)*(-A/2) ？那用迴圈怎麼做 ?
A = np.ones(3)*1
B = np.ones(3)*2
print(A) #[1. 1. 1.]
print(B) #[2. 2. 2.]
print((A+B)*(-A/2))
b=[]
for i in A :
    b.append((i+2*i)*(-i/2))
print(b)

# HW3 請問如何計算「1x6 的單位矩陣」和「6x1 的單位矩陣」的內積和外積？
A = np.ones((1,6))
B = np.ones((6,1))
print(A*B)
print(np.dot(A,B))

# 進階題
x=20*np.log10(20000/20)
print(x) # 60
# 50=20*np.log10(y/20)
y= 20*(10**2.5)
z= 20*(10**1.5)
print(y/z) #10倍