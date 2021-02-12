#1.   畫出 cos 圖檔，並儲存
# y = np.cos(x)
# 如果要存成圖形檔:
# 把 pyplot.show() 換成下面這行:
# plt.savefig("filename.png",dpi=300,format="png")

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,180) * np.pi / 180.0
y = np.cos(x)
plt.plot(x,y)
plt.savefig("cos.png",dpi=300,format="png")


#2.    給定散點圖顏色
import numpy as np
import matplotlib.pyplot as plt

n = 500
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.scatter(X, Y, marker='^', c='#64A600')
plt.show()
