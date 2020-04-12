import inline
import numpy as np
import matplotlib.pyplot as plt
from numpy import number

seed =1 # seed for random number generation
numInstances = 200 # number of data instances
np.random.seed(seed)
X = np.random.rand(numInstances,1).reshape(-1,1)
y_true = -3*X+1
y = y_true + np.random.normal(size=numInstances).reshape(-1,1)

plt.scatter(X,y,color='black')
plt.plot(X,y_true,color='blue',linewidth=3)
plt.title('True function: y = -3X + 1')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
