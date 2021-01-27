import numpy as np

# 1.將下兩列 array 存成 npz 檔 
array1 = np.array(range(30))
array2 = np.array([2,3,5])

with open('file1.npz', 'wb') as f:
    np.savez(f, array1, array2)


# 2.讀取剛剛的 npz 檔，加入下列 array 一起存成新的 npz 檔
array3 = np.array([[4,5,6], [1,2,3]])

temp_file = np.load('file1.npz')
t1 = temp_file['arr_0']
t2 = temp_file['arr_1']

with open('file2.npz', 'wb') as f:
    np.savez(f, t1, t2, array3)
