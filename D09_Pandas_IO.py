import pandas as pd
#讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案

output = pd.read_csv("boston.csv", usecols=["CHAS", "NOX", "RM"])
output.to_excel("boston.xlsx")
