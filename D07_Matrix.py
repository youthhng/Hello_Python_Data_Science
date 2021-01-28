import numpy as np
array1 = np.array([[10, 8], [3, 5]])
#[[10  8]
# [ 3  5]]

# 1.運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array2 = np.linalg.inv(array1)
#[[ 0.19230769 -0.30769231]
# [-0.11538462  0.38461538]]
np.matmul(array1, array2)
#[[1., 0.],
# [0., 1.]]


# 2.運用上列array計算特徵值、特徵向量?
w, v = np.linalg.eig(array1)
#w = [13.  2.]
#v = [[ 0.93632918 -0.70710678]
#     [ 0.35112344  0.70710678]]


# 3.運用上列array計算SVD?
np.linalg.matrix_rank(array1)
#2
