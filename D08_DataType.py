import numpy as np 

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

#1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
dt = np.dtype({'names':('name','sex','weight','rank','myopia'), 'formats':('U8', 'U8', 'f4', 'i2', '?')})
big_array = np.zeros(8, dtype=dt)

big_array['name'] = name_list
big_array['sex'] = sex_list
big_array['weight'] = weight_list
big_array['rank'] = rank_list
big_array['myopia'] = myopia_list

print(big_array)


#2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重

#3. 呈上題，進一步算出男生(sex欄位是boy)平均體重

#4. 呈上題，進一步算出女生(sex欄位是girl)平均體重
