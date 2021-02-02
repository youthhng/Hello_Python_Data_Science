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



#更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?
from sklearn.preprocessing import LabelEncoder
q_df['Sex_label'] = LabelEncoder().fit_transform(q_df['Sex']) #Sex可用順序性or一般性

q_df['Profession_label'] = LabelEncoder().fit_transform(q_df['Profession'].values) #Profession使用一般性
