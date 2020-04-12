import inline
import numpy as np
import matplotlib.pyplot as plt
from numpy import number
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

seed = 1
numInstances = 200 # number of data instances
np.random.seed(seed)
X = np.random.rand(numInstances,1).reshape(-1,1)
X2 = 0.5*X + np.random.normal(0,0.04,size=numInstances).reshape(-1,1)
X3 = 0.5*X2 + np.random.normal(0,0.01,size=numInstances).reshape(-1,1)
X4 = 0.5*X3 + np.random.normal(0,0.01,size=numInstances).reshape(-1,1)
X5 = 0.5*X4 + np.random.normal(0,0.01,size=numInstances).reshape(-1,1)

numTrain = 20 #number of training instances
numTest = numInstances - numTrain

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(12,9))
ax1.scatter(X,X2,color='black')
ax1.set_xlabel('X')
ax1.set_ylabel('X2')
c = np.corrcoef(np.column_stack((X[:-numTest],X2[:-numTest])).T)
titlestr = 'Correlation between X and X2 = &.4f' % (c[0,1])
ax1.set_title(titlestr)

ax2.scatter(X2,X3,color='black')
ax2.set_xlabel('X2')
ax2.set_ylabel('X3')
c = np.corrcoef(np.column_stack((X2[:-numTest],X3[:-numTest])).T)
titlestr = 'Correlation between X2 and X3 = &.4f' % (c[0,1])
ax2.set_title(titlestr)

ax3.scatter(X3,X4,color='black')
ax3.set_xlabel('X2')
ax3.set_ylabel('X4')
c = np.corrcoef(np.column_stack((X3[:-numTest],X4[:-numTest])).T)
titlestr = 'Correlation between X3 and X4 = &.4f' % (c[0,1])
ax3.set_title(titlestr)

ax4.scatter(X3,X4,color='black')
ax4.set_xlabel('X3')
ax4.set_ylabel('X4')
c = np.corrcoef(np.column_stack((X4[:-numTest],X5[:-numTest])).T)
titlestr = 'Correlation between X4 and X5 = &.4f' % (c[0,1])
ax4.set_title(titlestr)

plt.show()
