import numpy as np

x = np.arange(-5,5)
print(x)


y=x[3:5]  #y is a slice, i.e., pointer to a subarray in x
print(y)
y[:] = 1000  #modifying the value of y will change x
print(y)
print(x)

z = x[3:5].copy()  #makes a copy of the subarray
print(z)
z[:] = 500  #modifying the value of z will not affect x
print(z)
print(x)
