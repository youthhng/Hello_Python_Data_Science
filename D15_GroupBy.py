import pandas as pd
score_df = pd.DataFrame([[1,50,80,70,'boy',1], 
              [2,60,45,50,'boy',2],
              [3,98,43,55,'boy',1],
              [4,70,69,89,'boy',2],
              [5,56,79,60,'girl',1],
              [6,60,68,55,'girl',2],
              [7,45,70,77,'girl',1],
              [8,55,77,76,'girl',2],
              [9,25,57,60,'girl',1],
              [10,88,40,43,'girl',3],
              [11,25,60,45,'boy',3],
              [12,80,60,23,'boy',3],
              [13,20,90,66,'girl',3],
              [14,50,50,50,'girl',3],
              [15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])
#score_df

#1.找出全年級各科成績最高分與最低分?
#1.找出全年級各科成績最高分與最低分?
ma_max = score_df.max()['math_score']
ma_min = score_df.min()['math_score']
en_max = score_df.max()['english_score']
en_min = score_df.min()['english_score']
ch_max = score_df.max()['chinese_score']
ch_min = score_df.min()['chinese_score']

print("Math    max: %d, min: %d\nEnglish max: %d, min: %d\nChinese max: %d, min: %d" 
      %(ma_max, ma_min, en_max, en_min, ch_max, ch_min))

#Math    max: 98, min: 20
#English max: 90, min: 40
#Chinese max: 89, min: 23


#2.找出數學班平均最高的班級?
score_df.groupby('class').mean()['math_score']
#class
#1    54.800000
#2    61.250000
#3    58.666667
#Name: math_score, dtype: float64


#3.分析全校女生與男生國文平均差幾分?
score_df.groupby('sex').mean()['chinese_score']['girl'] - score_df.groupby('sex').mean()['chinese_score']['boy']
#7.333333333333329
