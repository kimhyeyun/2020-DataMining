from pandas import DataFrame

cars = {'make': ['Ford','Honda','Toyota','Tesla'],
        'model':['Taurus','Accord','Camry','Model S'],
        'MSRP' : [27595,23570,23495,68000]}
carData2 = DataFrame(cars,index = [1,2,3,4])    #change the row index
carData2['year'] = 2018 #ad column with same value
carData2['dealership'] = ['Courtesy Ford','Capital Honda','Spartan Toyota','N/A']

#selecting and filtering

print('carData2[carData2.MSRP >25000]')
print(carData2[carData2.MSRP>25000])
