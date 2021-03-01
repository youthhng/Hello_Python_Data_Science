#取得另一個 dataset：titanic

# 導入必要的程式庫
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# 取得資料集
df = sns.load_dataset('titanic')
df.info()


#Q1. 做箱形圖
sns.boxplot(data = df, orient = "h")


#Q2. 利用 facet grid 繪圖並分析
g = sns.FacetGrid(df, col="survived", row="sex")
g.map(sns.scatterplot, "pclass", "age")


#Q3. 繪製小提琴圖
sns.violinplot(x="pclass", y="age", data=df)
