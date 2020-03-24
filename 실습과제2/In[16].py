import numpy as np
from pandas import Series

s2 = Series(np.random.randn(6))     #creating a series from a numpy ndarray
print(s2)
print('Values = ',s2.values)        #display values of the Series
print('Index = ',s2.index)          #display indices of the Series

