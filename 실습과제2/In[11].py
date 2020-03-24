import numpy as np

x = np.arange(-2,3)
y = np.random.randn(5)
print(x)
print(y)

print(np.add(x,y))      #element-wise addition       x+y
print(np.subtract(x,y)) #element-wise subtraction    x-y
print(np.multiply(x,y)) #element-wise multiplication x*y
print(np.divide(x,y))   #element-wise division       x/y
print(np.maximum(x,y))  #element-wise maximum        max(x,y)