from pandas import DataFrame

cars = {'make': ['Ford','Honda','Toyota','Tesla'],
        'model':['Taurus','Accord','Camry','Model S'],
        'MSRP' : [27595,23570,23495,68000]}
carData2 = DataFrame(cars,index = [1,2,3,4])    #change the row index
carData2['year'] = 2018 #ad column with same value
carData2['dealership'] = ['Courtesy Ford','Capital Honda','Spartan Toyota','N/A']

#accessing a specific element of the DataFrame

print(carData2)
print(carData2.iloc[1,2])   #retrieving second row. third column
print(carData2.loc[1,'model'])  #retrieving second row. column named 'model'

#accessing a slice of the DataFrame

print('carData2.iloc[1:3,1:3] = ')
print(carData2.iloc[1:3,1:3])
