import numpy as np

print(np.random.rand(5))  #random numbers from a uniform distrubution between [0,1]
print(np.random.randn(5))  #random numbbers from a normal distribution
print(np.arange(-10,10,2)) #similar to range, but returns ndarray instead of list
print(np.arange(12).reshape(3,4)) #reshape to a matrix
print(np.linspace(0,1,10)) #split interval [0,1] into 10 equally separated values
print(np.logspace(-3,3,7))  #create ndarray with values from 10^-3 to 10^3