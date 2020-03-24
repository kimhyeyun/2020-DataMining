from pandas import DataFrame
import numpy as np

cars = {'make': ['Ford','Honda','Toyota','Tesla'],
        'model':['Taurus','Accord','Camry','Model S'],
        'MSRP' : [27595,23570,23495,68000]}
carData2 = DataFrame(cars,index = [1,2,3,4])    #change the row index
carData2['year'] = 2018 #ad column with same value
carData2['dealership'] = ['Courtesy Ford','Capital Honda','Spartan Toyota','N/A']

npdata = np.random.randn(5,3)   #create a 5 by 3 random matrix
columnNames = ['x1','x2','x3']
data = DataFrame(npdata,columns=columnNames)

#accessing an entire row will return a Series object

print('Row 3 of data table : ')
print(data.iloc[2])     #returns the 3rd row of DataFrame
print(type(data.iloc[2]))
print('\nRow 3 of car data table : ')
print(carData2.iloc[2]) #row contains objects of different types