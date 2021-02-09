import numpy as np
import pandas as pd
index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)
series

#1. 將所有轉為周資料
series.resample('W').asfreq()

#2. 將周資料的值取平均
series.resample('W').asfreq().mean()
