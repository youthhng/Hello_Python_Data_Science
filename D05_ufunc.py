english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

# Q1.請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略？
np.nanmean(english_score)
np.nanmean(math_score)
np.nanmean(chinese_score)

np.nanmax(english_score)
np.nanmax(math_score)
np.nanmax(chinese_score)

np.nanmin(english_score)
np.nanmin(math_score)
np.nanmin(chinese_score)

np.nanstd(english_score)
np.nanstd(math_score)
np.nanstd(chinese_score)

# Q2.第五位同學補考數學後成績為 55，請計算補考後數學成績平均、最大值、最小值、標準差？
math_score[4] = 55
np.mean(math_score)
np.max(math_score)
np.min(math_score)
np.std(math_score)

# Q3.用補考後資料找出與國文成績相關係數最高的學科
en_ch = np.corrcoef(english_score, chinese_score)
#array([[1.        , 0.97792828],
#       [0.97792828, 1.        ]])
ma_ch = np.corrcoef(math_score, chinese_score)
#array([[1.        , 0.74056803],
#       [0.74056803, 1.        ]])

np.max([en_ch[0,1], ma_ch[0,1]]) #0.977928283021127
