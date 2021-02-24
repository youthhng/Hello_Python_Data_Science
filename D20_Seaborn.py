import numpy as np
import seaborn as sns

#設定圖形樣式 - whitegrid
# use sns.set
sns.set(style="whitegrid")

# 利用 NUMPY 去建立資料集
# np.random.RandomState 設定數學式
rs = np.random.RandomState(100)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)

# 畫圖
sns.residplot(x, y, lowess=True, color="g")

###############

# bin: 指的是特徵值, 
# kde: on/off
# sns.distplot();
# sns.distplot(x, bins=, kde=, rug=);
sns.distplot(x, bins=25, kde=False, rug=True);
