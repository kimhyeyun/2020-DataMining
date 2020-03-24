import numpy as np

X = np.random.randn(5,3)
print(X)

C = X.T.dot(X)          # C = X^T * X is a square matrix

invC = np.linalg.inv(C) #inverse of a square matrix
print(invC)
detC = np.linalg.det(C) #determinant of a square matrix
print(detC)
S,U = np.linalg.eig(C)  #eigenvalue S and eigenvector U of a square matrix
print(S)
print(U)
