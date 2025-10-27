import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# -------------------- COLUMN SLICING --------------------

#print(array[:, 1])     
# All rows, column index 1 → second column
# Output:
# [ 2  6 10 14]

#print(array[:, 1:2])   
# All rows, column slice [1:2] → keeps 2D shape (a column vector)
# Output:
# [[ 2]
#  [ 6]
#  [10]
#  [14]]

#print(array[:, 1:3])   
# All rows, columns index 1 up to 3 (2nd and 3rd columns)
# Output:
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]

#print(array[:, 2:3])   
# All rows, column slice [2:3] → 3rd column in 2D format
# Output:
# [[ 3]
#  [ 7]
#  [11]
#  [15]]

#print(array[:, 1:4])   
# All rows, columns from 1 up to 4 (2nd → 4th columns)
# Output:
# [[ 2  3  4]
#  [ 6  7  8]
#  [10 11 12]
#  [14 15 16]]

#print(array[:, 1::-1]) 
# All rows, columns from 1 down to 0 (reversed: col 1 then col 0)
# Output:
# [[ 2  1]
#  [ 6  5]
#  [10  9]
#  [14 13]]

#print(array[:, 0::-1]) 
# All rows, from column 0 downwards (only column 0, reversed, but just itself)
# Output:
# [[ 1]
#  [ 5]
#  [ 9]
#  [13]]

# -------------------- ROW & COLUMN SLICING --------------------

#print(array[0:2, 1:2]) 
# Rows 0-1, column 1 only
# Output:
# [[2]
#  [6]]

#print(array[1:3, 1:3]) 
# Rows 1-2, columns 1-2
# Output:
# [[ 6  7]
#  [10 11]]

#print(array[2:4, 2:])  
# Rows 2-3, columns from 2 to end
# Output:
# [[11 12]
#  [15 16]]

print(array[1::2])  

#print(array[:, 1::2])  

#print(array[:, 1::2])  