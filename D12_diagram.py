import pandas as pd
read_boston = pd.read_csv("boston.csv")

#1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
df = pd.DataFrame(read_boston)
df.boxplot()
#ans: tax

#2.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
df.plot.scatter(x='NOX', y='DIS')
#ans: 呈現 y=1/x^n 的負相關
