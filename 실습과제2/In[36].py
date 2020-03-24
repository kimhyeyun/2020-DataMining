import numpy as np
from pandas import DataFrame

npdata = np.random.randn(5,3)   #create a 5 by 3 random matrix
columnNames = ['x1','x2','x3']
data = DataFrame(npdata,columns=columnNames)

print(data.abs())           #get the absolute value for each element

print("\nMaximum value per column : ")
print(data.max())           #get maximum value for each column

print('\nMinimum value per row : ')
print(data.min(axis=1))     #get minimum value for each row

print('\nSum of values per column : ')
print(data.sum())           #get sum of values for each column

print('\nAverage value per row : ')
print(data.mean(axis=1))    #get average value for each row

print('\nCalculate max - min per column')
f = lambda  x: x.max() - x.min()
print(data.apply(f))

print('\nCalculate max -  min per row')
f = lambda x: x.max() - x.min()
print(data.apply(f,axis=1))
