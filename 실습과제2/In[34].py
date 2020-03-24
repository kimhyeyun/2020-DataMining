import numpy as np
from pandas import DataFrame

npdata = np.random.randn(5,3)   #create a 5 by 3 random matrix
columnNames = ['x1','x2','x3']
data = DataFrame(npdata,columns=columnNames)
print(data)

print('Data transpose operation: ')
print(data.T)       #transpose operation

print('Addition: ')
print(data+4)       #addition operation

print('Multiplication: ')
print(data*10)      #multiplication operation