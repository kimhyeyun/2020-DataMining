import numpy as np

oneDim = np.array([1.0,2,3,4,5]) #a 1-dimensional array (vector)
print(oneDim)
print("#Dimensions = ",oneDim.ndim)
print("Dimenstion = ",oneDim.shape)
print("Size = ",oneDim.size)
print("Array type = ",oneDim.dtype)

twoDim = np.array([[1,2],[3,4],[5,6],[7,8]])  #a two-dimensional array (matrix)
print(twoDim)
print("#Dimensions = ",twoDim.ndim)
print("Dimension = ",twoDim.shape)
print("Size = ",twoDim.size)
print("Array type = ",twoDim.dtype)

arrFromTuple = np.array([(1,'a',3.0),(2,'b',3.5)]) #create ndarray from tuple
print(arrFromTuple)
print("#Dimensions = ",arrFromTuple.ndim)
print("Dimensions = ",arrFromTuple.shape)
print("Size = ",arrFromTuple.size)