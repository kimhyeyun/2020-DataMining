import numpy as np
from pandas import DataFrame

npdata = np.random.randn(5,3)   #create a 5 by 3 random matrix
columnNames = ['x1','x2','x3']
data = DataFrame(npdata,columns=columnNames)

#accessing an entire column will return a Series object

print(data['x2'])
print(type(data['x2']))
