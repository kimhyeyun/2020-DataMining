import numpy as np

X = np.random.randn(2,3)    #create a 2 x 3 random matrix
print(X)
print(X.T)      #matrix transpose operation X^T

y = np.random.randn(3)  #random vector
print(y)
print(X.dot(y))         #matrix-vector multiplication X*y
print(X.dot(y))         #matrix-matrix multiplication X*X^T
print(X.T.dot(X))       #matrix-matrix multiplication X^T*X
