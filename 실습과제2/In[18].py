from pandas import Series

capitals = {'MI':'Lansing','CA':'Sacramento','TX':'Austin','MN':'St Paul'}

s4 = Series(capitals)       #creating a series from dictionary object
print(s4)
print('Values = ',s4.values)    #display values of the Series
print('Index = ',s4.index)      #display indices of the Series