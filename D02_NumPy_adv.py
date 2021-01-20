# 題目：
# array1 = np.array(range(30))

# Q1.將上列陣列(array1)，轉成維度為(5X6)的 array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
b = array1.reshape(5,6).ravel(order='F').reshape(6,5)

array([[ 0,  6, 12, 18, 24],
       [ 1,  7, 13, 19, 25],
       [ 2,  8, 14, 20, 26],
       [ 3,  9, 15, 21, 27],
       [ 4, 10, 16, 22, 28],
       [ 5, 11, 17, 23, 29]])


# Q2. 呈上題的 array，找出被 6 除餘 1 的數的索引
np.where(b%6==1)

(array([1, 1, 1, 1, 1]), array([0, 1, 2, 3, 4]))
