import numpy as np

test_mat = [[1,2,3],[4,5,6]]

rows, columns = np.shape(test_mat)

for i in range(0, rows):
    for j in range(0, columns):
        print(test_mat[i][j])

