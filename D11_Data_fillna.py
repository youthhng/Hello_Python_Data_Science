import pandas as pd
q_df = pd.DataFrame([['male', 'teacher'], 
              ['male', 'engineer'],
              ['female', None],
              ['female', 'engineer']],columns=['Sex','Profession'])
#   Sex	    Profession
#0	male	  teacher
#1	male	  engineer
#2	female	None   ----> 沒有被判斷成NaN
#3	female	enginee

#缺失值填入字串'others'
q_df.fillna("others")
#   Sex	    Profession
#0	male	  teacher
#1	male	  engineer
#2	female	None   ----> 沒有被取代成"others"
#3	female	enginee


#更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?

#Sex可用順序性or一般性
from sklearn.preprocessing import LabelEncoder
q_df['Sex_label'] = LabelEncoder().fit_transform(q_df['Sex']) 

#Profession使用一般性
getDummies = pd.get_dummies(q_df['Profession']) #Profession使用一般性
pd.concat([q_df, getDummies], axis=1)

#   Sex	    Profession	Sex_label	None	engineer	teacher
#0	male	  teacher	    1	        0	    0	        1
#1	male	  engineer	  1	        0	    1	        0
#2	female	None	      0	        1	    0	        0
#3	female	engineer	  0	        0	    1	        0
