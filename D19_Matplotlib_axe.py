### Q1 ###
import matplotlib.pyplot as plt

#決定底框
plt.axes([0.1,0.1,.5,.5])
#給定刻度
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)

#決定第二層框
plt.axes([0.2,0.2,.5,.5])
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.2,0.2,.5,.5])',ha='left',va='center',size=16,alpha=.5)

#決定第三層框
plt.axes([0.3,0.3,.5,.5])
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.3,0.3,.5,.5])',ha='left',va='center',size=16,alpha=.5)

#決定第四層框
plt.axes([0.4,0.4,.5,.5])
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.4,0.4,.5,.5])',ha='left',va='center',size=16,alpha=.5)

plt.show()




### Q2 ###
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
plt.bar(X, -Y2, facecolor='#FF60AF', edgecolor='white')
# +Y 指的是 XY 四象限的第一象限

'''
#指定上半部繪製區域, 給定 Bar 顏色, 邊界顏色
'''

 #設定繪圖圖示區間
for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')
    
#for x,y in zip(X,Y2):
    #plt.text(x+0.4, (y+0.05)*-1, '%.2f' % y, ha='center', va= 'bottom')   

#設定Y軸區間
plt.ylim(-1.25,+1.25)
plt.show()
