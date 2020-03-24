import numpy as np

my2darr = np.arange(1,13,1).reshape(4,3)
print(my2darr)

indices = [2,1,0,3]     #selected row indices
print(my2darr[indices,:])

rowIndex = [0,0,1,2,3]  #row index into my2darr
columnIndex = [0,2,0,1,2]   #column index into my2darr
print(my2darr[rowIndex,columnIndex])