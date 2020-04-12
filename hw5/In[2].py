import inline
import numpy as np
import matplotlib.pyplot as plt
from numpy import number
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

seed =1 # seed for random number generation
numInstances = 200 # number of data instances
np.random.seed(seed)
X = np.random.rand(numInstances,1).reshape(-1,1)
y_true = -3*X+1
y = y_true + np.random.normal(size=numInstances).reshape(-1,1)

numTrain = 20 #number of training instances
numTest = numInstances - numTrain

X_train = X[:-numTest]
X_test = X[-numTest:]
y_train = y[:-numTest]
y_test = y[-numTest:]

#Create linear regression object
regr = linear_model.LinearRegression()

#Fit regression model to the training set
regr.fit(X_train,y_train)

print(regr)
