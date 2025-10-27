import numpy as np

array = np.array([[
                    [ 'A', 'B', 'C'], [ 'D', 'E', 'F'], [ 'G', 'H', 'I']],
                  [
                    [ 'J', 'K', 'L'], [ 'M', 'N', 'O'], [ 'P', 'Q', 'R']],
                  [
                    [ 'S', 'T', 'U'], [ 'V', 'W', 'X'], [ 'Y', 'Z', '_']]
                  
                  ])

print(array.shape) 
# layer rows columns
print(array[2][2][2]) # chain indexing

word = array[0,0,0] + array[2,0,0] + array[2,0,0]

print(word)