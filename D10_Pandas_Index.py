import pandas as pd
#讀取STOCK_DAY_0050_202009.csv、STOCK_DAY_0050_202010.csv
stock_09 = pd.read_csv('STOCK_DAY_0050_202009.csv')
stock_10 = pd.read_csv('STOCK_DAY_0050_202010.csv')

#串聯
stock_09_10 = pd.concat([stock_09,stock_10])

#找出open小於close的資料
pd.DataFrame(data=stock_09_10).loc[stock_09_10.open < stock_09_10.close]
#stock_09_10[stock_09_10.open < stock_09_10.close]
