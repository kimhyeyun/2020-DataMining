import inline
import numpy as np
import matplotlib.pyplot as plt
from numpy import number
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

seed = 1
numInstances = 200 # number of data instances
np.random.seed(seed)
X = np.random.rand(numInstances,1).reshape(-1,1)
y_true = -3*X+1
y = y_true + np.random.normal(size=numInstances).reshape(-1,1)

X2 = 0.5*X + np.random.normal(0,0.04,size=numInstances).reshape(-1,1)
X3 = 0.5*X2 + np.random.normal(0,0.01,size=numInstances).reshape(-1,1)
X4 = 0.5*X3 + np.random.normal(0,0.01,size=numInstances).reshape(-1,1)
X5 = 0.5*X4 + np.random.normal(0,0.01,size=numInstances).reshape(-1,1)

numTrain = 20 #number of training instances
numTest = numInstances - numTrain

X_train = X[:-numTest]
X_test = X[-numTest:]
y_train = y[:-numTest]
y_test = y[-numTest:]

X_train2 = np.column_stack((X[:-numTest],X2[:-numTest]))
X_test2 = np.column_stack((X[-numTest:],X2[-numTest:]))
X_train3 = np.column_stack((X[:-numTest],X2[:-numTest],X3[:-numTest]))
X_test3 = np.column_stack((X[-numTest:],X2[-numTest:],X3[-numTest:]))
X_train4 = np.column_stack((X[:-numTest],X2[:-numTest],X3[:-numTest],X4[:-numTest]))
X_test4 = np.column_stack((X[-numTest:],X2[-numTest:],X3[-numTest:],X4[-numTest:]))
X_train5 = np.column_stack((X[:-numTest],X2[:-numTest],X3[:-numTest],X4[:-numTest],X5[:-numTest]))
X_test5 = np.column_stack((X[-numTest:],X2[-numTest:],X3[-numTest:],X4[-numTest:],X5[-numTest:]))

regr = linear_model.LinearRegression()
regr.fit(X_train,y_train)
regr2 = linear_model.LinearRegression()
regr2.fit(X_train2,y_train)
regr3 = linear_model.LinearRegression()
regr3.fit(X_train3,y_train)
regr4 = linear_model.LinearRegression()
regr4.fit(X_train4,y_train)
regr5 = linear_model.LinearRegression()
regr5.fit(X_train5,y_train)

y_pred_train = regr.predict(X_train)
y_pred_test = regr.predict(X_test)
y_pred_train2 = regr2.predict(X_train2)
y_pred_test2 = regr2.predict(X_test2)
y_pred_train3 = regr3.predict(X_train3)
y_pred_test3 = regr3.predict(X_test3)
y_pred_train4 = regr4.predict(X_train4)
y_pred_test4 = regr4.predict(X_test4)
y_pred_train5 = regr5.predict(X_train5)
y_pred_test5 = regr5.predict(X_test5)

columns = ['Model','Train error','Test error','Sum of Absolute Weights']
model1 = "%.2f X + %.2f" % (regr.coef_[0][0], regr.intercept_[0])
values1 = [model1,np.sqrt(mean_squared_error(y_train,y_pred_train)),
           np.sqrt(mean_squared_error(y_test,y_pred_test)),
           np.absolute(regr.coef_[0].sum()+np.absolute(regr.intercept_[0]))]
model2 = "%.2f X + %.2f X2 + %.2f" % (regr2.coef_[0][0], regr2.coef_[0][1], regr2.intercept_[0])
values2 = [model2,np.sqrt(mean_squared_error(y_train,y_pred_train2)),
           np.sqrt(mean_squared_error(y_test,y_pred_test2)),
           np.absolute(regr2.coef_[0].sum()+np.absolute(regr2.intercept_[0]))]
model3 = "%.2f X + %.2f X2 + %.2f X3 + %.2f" % (regr3.coef_[0][0], regr3.coef_[0][1],regr3.coef_[0][2], regr3.intercept_[0])
values3 = [model3,np.sqrt(mean_squared_error(y_train,y_pred_train3)),
           np.sqrt(mean_squared_error(y_test,y_pred_test3)),
           np.absolute(regr3.coef_[0].sum()+np.absolute(regr3.intercept_[0]))]
model4 = "%.2f X + %.2f X2 + %.2f X3 + %.2f X4 + %.2f" % (regr4.coef_[0][0], regr4.coef_[0][1],regr4.coef_[0][2]
                                                          ,regr4.coef_[0][3], regr4.intercept_[0])
values4 = [model4,np.sqrt(mean_squared_error(y_train,y_pred_train4)),
           np.sqrt(mean_squared_error(y_test,y_pred_test4)),
           np.absolute(regr4.coef_[0].sum()+np.absolute(regr4.intercept_[0]))]
model5 = "%.2f X + %.2f X2 + %.2f X3 + %.2f X4 + %.2f X5 + %.2f" % (regr5.coef_[0][0], regr5.coef_[0][1],regr5.coef_[0][2]
                                                          ,regr5.coef_[0][3], regr5.coef_[0][4], regr5.intercept_[0])
values5 = [model5,np.sqrt(mean_squared_error(y_train,y_pred_train5)),
           np.sqrt(mean_squared_error(y_test,y_pred_test5)),
           np.absolute(regr5.coef_[0].sum()+np.absolute(regr5.intercept_[0]))]

results = pd.DataFrame([values1,values2,values3,values4,values5],columns=columns)

plt.plot(results['Sum of Absolute Weights'],results['Train error'],'ro-')
plt.plot(results['Sum of Absolute Weights'],results['Test error'],'k*--')
plt.legend(['Train error','Test error'])
plt.xlabel('Sum of Absolute Weights')
plt.ylabel('Error rate')

print(results)
plt.show()


