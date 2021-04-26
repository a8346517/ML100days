import matplotlib.pyplot as plt
#決定底框
plt.axes([0.1,0.1,.5,.5])
#給定刻度, 若不給定值, 圖的周邊無文字
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)


#第2層框
plt.axes([0.2,0.2,.4,.4])
plt.xticks([]),plt.yticks([])
plt.text(0.1,0.1,'axes([0.2,0.2,.4,.4])',ha='left',va='center',size=12,alpha=.5)

#第3層框
plt.axes([0.3,0.3,.3,.3])
plt.xticks([]),plt.yticks([])
plt.text(0.1,0.1,'axes([0.3,0.3,.3,.3])',ha='left',va='center',size=8,alpha=.5)
#第四層框
plt.axes([0.4,0.4,.2,.2])
plt.xticks([]),plt.yticks([])
plt.text(0.1,0.1,'axes([0.4,0.4,.2,.2])',ha='left',va='center',size=4,alpha=.5)
plt.show()

# 嘗試通過添加紅色條形標籤重現上側的圖形。
import numpy as np
import matplotlib.pyplot as plt

 #配置12 組 Bar
n = 12 
X = np.arange(n)

 #給定數學運算式
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
#指定上半部繪製區域, 給定 Bar 顏色, 邊界顏色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='red', edgecolor='white')
# 設定繪圖圖示區間
for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')
for x,y in zip(X,-Y2):
    plt.text(x, y-0.1, '%.2f' % y, ha='center', va= 'bottom')
 #設定Y軸區間
plt.ylim(-1.25,+1.25)
plt.show()

