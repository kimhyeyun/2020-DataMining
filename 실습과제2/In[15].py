from pandas import Series

s = Series([3.1,2.4,-1.7,0.2,-2.9,4.5])     #creating a series from a list
print(s)
print('Values = ',s.values)     #display values of the Series
print('Index = ',s.index)       #display indices of the Series